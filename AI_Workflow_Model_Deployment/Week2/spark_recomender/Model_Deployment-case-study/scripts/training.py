
import os
import shutil
import pandas as pd
import numpy as np
import pyspark as ps
from pyspark.ml import Pipeline
from pyspark.sql import Row
from pyspark.sql.types import DoubleType
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS

DATA_DIR = os.path.join(".", "/content/data/")
SAVE_DIR = os.path.join(".", "saved-recommender/")

if os.path.isdir(SAVE_DIR):
    shutil.rmtree(SAVE_DIR)



## ensure the spark context is available
spark = (ps.sql.SparkSession.builder
        .appName("sandbox")
        .getOrCreate()
        )

sc = spark.sparkContext
print(spark.version) 

movielens_data_dir = os.path.join(DATA_DIR, "ml-latest")   
print(movielens_data_dir) 
if not os.path.exists(movielens_data_dir):
    print("ERROR make sure the path to the Movie Lens data is correct")

## load the ratings data as a pysaprk dataframe
ratings_file = os.path.join(movielens_data_dir, "ratings.csv")
df = spark.read.format("csv").options(header="true", inferSchema="true").load(ratings_file)
df = df.withColumnRenamed("movieID", "movie_id")
df = df.withColumnRenamed("userID", "user_id")
df.show(n=2)

## load the movies data as a pyspark dataframe
movies_file = os.path.join(movielens_data_dir, "movies.csv") 
movies_df = spark.read.format("csv").options(header="true", inferSchema="true").load(movies_file)
movies_df = movies_df.withColumnRenamed("movieID", "movie_id")
movies_df.show(n=2)
df.describe().show()

(training, test) = df.randomSplit([0.8, 0.2])




def train_model(reg_param, implicit_prefs=False):
    """
    Train and evaluate an ALS model
    Inputs : the regularization parametre of the ALS model and the implicit_prefs flag
    Ouptus : a string with the RMSE and the regularization parameter inputed
    """
    
    als = ALS(regParam= reg_param, userCol="user_id", itemCol="movie_id", ratingCol="rating",
          coldStartStrategy="drop", implicitPrefs  = implicit_prefs)
    model = als.fit(training)

    predictions = model.transform(test)
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                predictionCol="prediction")

    rmse = evaluator.evaluate(predictions)
    print("regParam={}, RMSE={}".format(reg_param, np.round(rmse, 2)))


for reg_param in [0.01, 0.05, 0.1, 0.15, 0.25]:
    train_model(reg_param)


## YOUR CODE HERE
als = ALS(regParam= 0.05, userCol="user_id", itemCol="movie_id", ratingCol="rating",
          coldStartStrategy="drop", implicitPrefs  = True)
model = als.fit(training)

predictions = model.transform(test)
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                            predictionCol="prediction")

rmse = evaluator.evaluate(predictions)
print("regParam={}, RMSE={}".format(reg_param, np.round(rmse, 2)))


print("...saving als model")
model.save(SAVE_DIR + '/model_1')
print("done.")



