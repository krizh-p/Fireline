from pymongo import MongoClient
import sklearn
from sklearn import linear_model

client = MongoClient("mongodb+srv://sabdulb:sabdulb@fireeye.aw4lhpu.mongodb.net/")

db = client.get_database('wildfire_db')

records = db.wildfire_data
query = {"FIRE_NAME": {"$exists": True}}
data = records.find(query)
fire_list = []
for fire in data:
    fire_location = {"NAME": fire["FIRE_NAME"], "YEAR": fire["FIRE_YEAR"], "STATE": fire["STATE"], "LONG": fire["LONGITUDE"], "LAT": fire["LATITUDE"]}
    fire_list.append(fire_location)

print(fire_list)