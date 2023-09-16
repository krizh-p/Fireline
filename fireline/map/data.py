from pymongo import MongoClient

client = MongoClient("mongodb+srv://sabdulb:sabdulb@fireeye.aw4lhpu.mongodb.net/")

db = client.get_database('wildfire_db')

records = db.wildfire_data

print(records.count_documents({}))