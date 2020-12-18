
import os
import sys
import getopt
import pandas as pd
import numpy as np
import sqlite3

DATA_DIR = os.path.join(".","data")

def connect_db(file_path):
    """
    function to connection to aavail database
    """
    try:
        conn = sqlite3.connect(file_path)
        print("...successfully connected to db")
    except Error as e:
        print("...unsuccessful connection", e)
    
    return(conn)

def ingest_db_data(conn):
    """
    load and clean the db data
    """
    
    query = """
    SELECT cu.customer_id, cu.last_name, cu.first_name, cu.DOB,
           cu.city, cu.state, co.country_name, cu.gender
    FROM CUSTOMER cu
    INNER JOIN COUNTRY co
    ON cu.country_id = co.country_id;
    """
    df_db = pd.read_sql_query(query, conn)
    
    # Remove duplicates
    size_before = len(df_db)
    df_db.drop_duplicates(subset='customer_id', keep="first", inplace=True )
    size_after = len(df_db)
    print("... removed {} duplicate rows in db data".format(size_before-size_after))
    return df_db

def ingest_stream_data(file_path):
    """
    load and clean the stream data
    """
    
    df_streams = pd.read_csv(file_path)  
    size_before = len(df_streams)
    df_streams = df_streams[~df_streams['stream_id'].isna()]
    size_after = len(df_streams)
    print("... removed {} missing stream ids".format(size_before-size_after))

    has_churned = df_streams.groupby("customer_id").apply(lambda x : True if x['subscription_stopped'].max() > 0 else False)
    
    return df_streams, has_churned

def process_dataframes(df_db, df_streams, has_churned, conn):
    """
    add data to target csv
    """
    df_clean = df_db[df_db['customer_id'].isin(df_streams['customer_id'].unique())].copy()

    # Create customer_name column
    df_clean['customer_name'] = df_clean['first_name'] +' '+ df_clean['last_name']

    # Create age column from DOB
    DT = pd.Timestamp('now')
    df_clean['DOB'] = pd.to_datetime(df_clean['DOB'], format='%m/%d/%y') 
    df_clean['DOB'] = df_clean['DOB'].where(df_clean['DOB'] < DT, df_clean['DOB'] -  np.timedelta64(100, 'Y'))
    df_clean['age'] = (DT - df_clean['DOB']).astype('<m8[Y]')

    # Create is_subscriber column 
    df_clean['is_subscriber'] = df_clean.apply(lambda x : ~has_churned[x['customer_id']], axis=1)

    # Create num_streams column
    df_num_streams_tmp = df_streams.groupby('customer_id')\
                                    .size()\
                                    .reset_index()
    df_num_streams_tmp.columns = ['customer_id', 'num_streams']
    df_clean = df_clean.merge(df_num_streams_tmp, on='customer_id')

    del df_num_streams_tmp

    # Create subscryber type column
    query = """
    SELECT i.invoice_item_id, i.invoice_item
    FROM INVOICE_ITEM i;
    """
    df_invoice = pd.read_sql_query(query, conn)

    df_invoice_type_tmp = df_streams[['customer_id', 'invoice_item_id']].groupby('customer_id')\
                                                                        .agg(lambda x:x.value_counts().index[0])\
                                                                        .reset_index()
    df_invoice_type_tmp = df_invoice_type_tmp.merge(df_invoice, on='invoice_item_id').drop('invoice_item_id', axis=1)
    df_invoice_type_tmp.columns = ['customer_id', 'subscriber_type']
    df_clean = df_clean.merge(df_invoice_type_tmp, on='customer_id')

    del df_invoice_type_tmp


    # Select the desired columns and copy to df_clean.
    columns_name = ['customer_id', 'country_name', 'age', 'customer_name', 'is_subscriber', 'subscriber_type', 'num_streams']
    df_clean = df_clean[columns_name]
    
    return(df_clean)
    
def update_target(target_file,
                  df_clean, overwrite=False):
    """
    update line by line in case data are large
    """

    if overwrite or not os.path.exists(target_file):
        df_clean.to_csv(target_file, index=False)   
    else:
        df_clean.to_csv(target_file, mode='a', header=False, index=False)
        
        
        
if __name__ == "__main__":
  
    ## collect args
    arg_string = "%s -d db_filepath -s streams_filepath"%sys.argv[0]
    try:
        optlist, args = getopt.getopt(sys.argv[1:],'d:s:')
    except getopt.GetoptError:
        print(getopt.GetoptError)
        raise Exception(arg_string)

    ## handle args
    streams_file = None
    db_file = None
    for o, a in optlist:
        if o == '-d':
            db_file = a
        if o == '-s':
            streams_file = a
    streams_file = os.path.join(DATA_DIR,streams_file)
    db_file = os.path.join(DATA_DIR,db_file)
    target_file = os.path.join(DATA_DIR, "aavail-target.csv")
    
    ## make the connection to the database
    conn = connect_db(db_file)

    ## ingest data base data
    df_db = ingest_db_data(conn)
    df_streams, df_churn = ingest_stream_data(streams_file)
    df_clean = process_dataframes(df_db, df_streams, df_churn, conn)
    
    ## write
    update_target(target_file, df_clean, overwrite=False)
    print("done")
