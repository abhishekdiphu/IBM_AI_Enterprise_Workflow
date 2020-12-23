 

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

######## NOTE ########
# Most of the code in this file is from make-happiness-summary-plot.py
# which is available as part of the case study.
# Code used in the solution to: ** QUESTION: Correlation plot **
# is labeled with that comment.
######################

import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## plot style and fonts
plt.style.use('seaborn')

SMALL_SIZE = 12
MEDIUM_SIZE = 14
LARGE_SIZE = 16

BLUE = "#0066FF"
ORANGE = "#FF6600"
GREY = "#777777"

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=LARGE_SIZE)   # fontsize of the figure title


DATA_DIR = os.path.join("..","data") 
IMAGE_DIR = os.path.join("..","images")


######## SOLUTION FUNC ####################
######## QUESTION: Correlation plot #######

## New import (should move this to the rest of the imports)
import seaborn as sns

def create_correlation_grid_plot(df, columns):
    """
    Create correlation grid using data from DataFrame df, specify which 
    columns to display with columns param. 

    Inspired by: https://seaborn.pydata.org/examples/many_pairwise_correlations.html
    """

    # Compute the correlation matrix
    corr = df[columns].corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    image_path = os.path.join(IMAGE_DIR,"happiness-corr-grid.png")    
    plt.savefig(image_path,bbox_inches='tight',pad_inches = 0,dpi=500)
    print("{} created.".format(image_path))

######### END: SOLUTION FUNC #############    

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
    
if __name__ == "__main__":

    
    df = run_data_ingestion()
    numeric_columns = ['Happiness_Score','Economy_(GDP_per_Capita)', 'Family',
                      'Health_(Life_Expectancy)', 'Freedom', 
                      'Trust_(Government_Corruption)', 'Generosity',
                      'Dystopia_Residual'] 
    create_correlation_grid_plot(df, numeric_columns)
