#!/usr/bin/env python

"""

ABOUT:
    example script to create a summary plot from world happiness data

DATA:
    data produced by: http://unsdsn.org/about-us/vision-and-organization
    data compilied from: https://worldhappiness.report


DIRECTORIES
    You can modify the DATA_DIR and IMAGE_DIR directly or create a directory called 'data'
    and another called 'images'.  Ensure the csv file is in the data dir

"""

import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## plot style, fonts and colors
plt.style.use('seaborn')

SMALL_SIZE = 12
MEDIUM_SIZE = 14
LARGE_SIZE = 16
COLORS = ["darkorange","royalblue","slategrey"]

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=LARGE_SIZE)   # fontsize of the figure title

DATA_DIR = os.path.join("..","data") 
IMAGE_DIR = os.path.join("..","images")


def run_data_ingestion():
    """
    ready the data for EDA
    """

    print("... data ingestion")
    
    ## load the data and print the shape
    df = pd.read_csv(os.path.join(DATA_DIR,"world-happiness.csv"),index_col=0)

    ## clean up the column names
    df.columns = [re.sub("\s+","_",col) for col in df.columns.tolist()]

    ## drop the rows that have NaNs
    df.dropna(inplace=True)

    ## sort the data for more intuitive visualization
    df.sort_values(['Year', "Happiness_Score"], ascending=[True, False], inplace=True)

    return(df)

def create_subplot(table,ax):
    """
    create a subplot
    """

    table['average'] = (table[2015] + table[2016] + table[2017]) / 3
    regions = np.array(list(table.index))
    year_2015 = table[2015].values
    year_2016 = table[2016].values
    year_2017 = table[2017].values
    averages = table['average'].values
    sorted_inds = np.argsort(averages)

    ## make bar plot 
    N = regions.size
    ind = np.arange(N)
    width = 0.3
    rects1 = ax.bar(ind, year_2015[sorted_inds], width, color=COLORS[0], label='2015')
    rects2 = ax.bar(ind+width, year_2016[sorted_inds], width, color=COLORS[1], label='2016')
    rects3 = ax.bar(ind+width+width, year_2017[sorted_inds], width, color=COLORS[2], label='2017')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(regions[sorted_inds],rotation=90)
    ax.legend(loc='upper left')

def create_plot(df):
    """
    create a two panel subplot that summarizes two features of the data with respect to Year and Region
    """

    print("... creating plot")
    
    columns_to_show = ["Happiness_Score","Health_(Life_Expectancy)"]
    pd.pivot_table(df, index= 'Year',values=columns_to_show,aggfunc='mean').round(3)

    ## ready a figure
    fig = plt.figure(figsize=(9,6))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ## create first subplot
    table1 = pd.pivot_table(df,index='Region',columns='Year',values="Happiness_Score")
    create_subplot(table1,ax1)
    ax1.set_ylabel("Happiness Score")
    ax1.set_ylim((0,8.0))
    
    ## create second subplot
    table2 = pd.pivot_table(df,index='Region',columns='Year',values="Health_(Life_Expectancy)")
    create_subplot(table2,ax2)
    ax2.set_ylabel("Health (Life Expectancy)")
    ax2.set_ylim((0,1.0))
    
    ## ensure equal aspect ratio
    for ax in [ax1,ax2]:
        ax.set_aspect(1./ax.get_data_ratio()) 

    image_path = os.path.join(IMAGE_DIR,"happiness-summary.png")
    plt.savefig(image_path,bbox_inches='tight',pad_inches = 0,dpi=200)
    print("{} created.".format(image_path))
    
if __name__ == "__main__":

   df = run_data_ingestion()
   create_plot(df)
