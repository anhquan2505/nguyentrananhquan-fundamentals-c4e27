from pymongo import MongoClient
from faker import Faker
from random import randint, choice
faker = Faker()

mongo_uri= "mongodb+srv://admin:admin@c4e27-cluster-dgk4w.mongodb.net/test?retryWrites=true"
client= MongoClient(mongo_uri)
pilot_app = client.pilot

Service = pilot_app["service"]
