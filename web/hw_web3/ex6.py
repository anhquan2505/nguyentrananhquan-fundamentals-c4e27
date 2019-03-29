from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

db_demo = client.get_database()
rivers = db_demo["river"]
song =rivers.find()

africa=[]
for river in song:
    if river["continent"]== "Africa":
        africa.append(river["name"])
print(africa)
