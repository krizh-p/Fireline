from typing import List
from pymongo import MongoClient

#Access Database
client = MongoClient("mongodb+srv://sabdulb:sabdulb@fireeye.aw4lhpu.mongodb.net/")
db = client.get_database('wildfire_db')
records = db.wildfire_data
#Query to select map values
query = {"FIRE_NAME": {"$exists": True}}
def map_data() -> List[dict]:
    data = records.find(query)
    fire_list = []
    i = 0
    for fire in data:
        if i > 500:
          break
        fire_location = {"NAME": fire["FIRE_NAME"], "YEAR": fire["FIRE_YEAR"], "STATE": fire["STATE"], "LONG": fire["LONGITUDE"], "LAT": fire["LATITUDE"]}
        fire_list.append(fire_location)
        i += 1
    return fire_list
 

def prediction_data() -> List[dict]:
    data = records.find(query)
    fire_list = []
    for fire in data:
        fire_location = {"NAME": fire["FIRE_NAME"], "YEAR": fire["FIRE_YEAR"], "STATE": fire["STATE"], "LONG": fire["LONGITUDE"], "LAT": fire["LATITUDE"]}
        fire_list.append(fire_location)
    return fire_list

