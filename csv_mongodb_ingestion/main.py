import pandas as pd
from pymongo import MongoClient
# connect to "jsonIngestion" db
my_client = MongoClient("mongodb+srv://taleb:12345@json-ingestion.hlclrrf.mongodb.net/test")
# create table named "People"
db = my_client["People"]
# read csv file
info = pd.read_csv("grades.csv")
# convert csv to json
data = info.to_dict(orient="records")
# call db and name collection "Info"
# using insert_many() method since csv file contains multiple documents
# save data to db
db.Info.insert_many(data)
