    
from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = "mongodb+srv://admin:admin@c4e27-cluster-dgk4w.mongodb.net/test?retryWrites=true"
client= MongoClient(mongo_uri)
pilot_app = client.bike

OurBikes = pilot_app["Our Bikes"]
