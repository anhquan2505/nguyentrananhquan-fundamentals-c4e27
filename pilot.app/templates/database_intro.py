from pymongo import MongoClient
from bson.objectid import ObjectId

# 1) connect mongo database (mongodb)
mongo_uri = "mongodb+srv://admin:admin@c4e27-cluster-dgk4w.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

# 2) get/create database:
db_demo = client.database

# 3) get/create collection
first_connection = db_demo["my_collection"]

# # 4) create document
gaem_document = {
    "title" : "PUBG",
    "description" : "PlayerUnknown BattleGround",
    "number of gamers per team": 4
}

# # 5) insert document
first_connection.insert_one(gaem_document)

# 6) read
    # 6.1 read all
all_document=first_connection.find()
for document in all_document:
    print(document["title"])
    # 6.2 read one
one_document = first_connection.find_one({"title":"LoL"})
# find one chỉ tìm đc cái đầu tiên nếu có nhiều cái, còn find all nếu cho đk sẽ tìm toàn bộ
print(one_document)
# btvn cấp cho 1 dường link có sẵn

# 7) delete
delete_document = first_connection.find_one({"_id": ObjectId("5c979cc74614220ad0799816")})
if delete_document is not None:

    first_connection.delete_one(delete_document)
    print("deleted")
else:
    print("not found")
# 8) update
first_connection.find_one_and_replace(
    {"_id":ObjectId("5c9ce2e04614222ac023ed34")},{"title":"đp pubg"})


    