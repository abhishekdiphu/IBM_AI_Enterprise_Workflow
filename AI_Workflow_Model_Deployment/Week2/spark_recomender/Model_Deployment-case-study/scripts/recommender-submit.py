import os
import sys
from collections import Counter
import numpy as np
from pyspark.ml.recommendation import ALS, ALSModel
import pyspark as ps

SAVE_DIR = os.path.join("..", "saved-recommender")

spark = (ps.sql.SparkSession.builder
        .appName("recommend")
        .getOrCreate()
        )

sc = spark.sparkContext

## load saved model
model = ALSModel.load(SAVE_DIR)

## compile some movie ratings these are taken from the top ten (movie_id, title, rating)
new_ratings = [(1210, "Episode VI - Return of the Jedi (1983)", 5),
               (179819, "Star Wars: The Last Jedi (2017)", 5),
               (187595, "Solo: A Star Wars Story (2018)", 5),
               (122886, "Star Wars: Episode VII - The Force Awakens (2015)", 5),
               (1196, "Star Wars: Episode V - The Empire Strikes Back (1980)", 5),
               (2628, "Star Wars: Episode I - The Phantom Menace (1999)", 5),
               (260, "Star Wars: Episode IV - A New Hope (1977)", 5)]

new_ratings = sorted(new_ratings, key=lambda tup: tup[2])[::-1]
best_rated = [(nr[0],) for nr in new_ratings]
print('best rated', best_rated)
rated_movies = np.array([nr[0] for nr in new_ratings])

## query the model and find the closest k users
query1 = spark.createDataFrame(best_rated, ["movie_id"])
user_recs = model.recommendForItemSubset(query1, 100)
user_recs = user_recs.toPandas()

urecs = Counter()
for u in user_recs['recommendations']:
    for rec in u:
        rec = tuple(rec.asDict().values())
        urecs[rec[0]] += rec[1]

closest_users = [(ur[0],) for ur in urecs.most_common()]
print("closest_users\n", closest_users)

