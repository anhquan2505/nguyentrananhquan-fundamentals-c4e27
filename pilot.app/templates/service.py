from pymongo import MongoClient
from faker import Faker
from random import randint, choice
faker = Faker()

mongo_uri= "mongodb+srv://admin:admin@c4e27-cluster-dgk4w.mongodb.net/test?retryWrites=true"
client= MongoClient(mongo_uri)
pilot_app = client.pilot

service = pilot_app["service"]
for i in range (50):
    new_service = {
        "name": faker.name(),
        "age":randint(18,30),
        "gender":choice(["male","female"]),
        "height":randint(160,180),
        "available": choice([True, False]),
        "address":faker.address(),
    }

    service.insert_one(new_service)
    print("saving document {0}......", format(i+1))