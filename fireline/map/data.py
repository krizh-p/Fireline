from typing import List
from pymongo import MongoClient

#Access Database
client = MongoClient("mongodb+srv://sabdulb:sabdulb@fireeye.aw4lhpu.mongodb.net/")
db = client.get_database('wildfire_db')
records = db.wildfire_data
#Query to select map values
query = {"FIRE_NAME": {"$exists": True}}
data = records.find(query)
def map_data() -> List[dict]:
    fire_list = []
    i = 0
    for fire in data:
        if i > 500:
          break
        fire_location = {"NAME": fire["FIRE_NAME"], "YEAR": fire["FIRE_YEAR"], "STATE": fire["STATE"], "LONG": fire["LONGITUDE"], "LAT": fire["LATITUDE"]}
        fire_list.append(fire_location)
        i += 1
    return fire_list
 

def prediction_data() -> dict[List]:
    fire_dict = {}
    #Create lists of lattitudes and longitudes
    fire_lng = []
    fire_lat = []
    i = 0
    for fire in data:
        if i > 500:
            break

        if fire["STATE"] == "CA" or fire["STATE"] == "WA":
            fire_lng.append(fire["LONGITUDE"])
            fire_lat.append(fire["LATITUDE"])
        i+=1
    
    #Create dictionary of size 2, with LONG and LAT, each w/ a list value
    fire_dict["LONG"] = fire_lng
    fire_dict["LAT"] = fire_lat

    return fire_dict
