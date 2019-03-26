from pymongo import MongoClient


# 1) connect mongo database (mongodb)
mongo_uri = "mongodb+srv://admin:admin@c4e27-cluster-dgk4w.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

# 2) get/create database:
db_demo = client.database

# 3) get/create collection
first_connection = db_demo["my_collection"]

# # 4) create document
# gaem_document = {
#     "title" : "PUBG",
#     "description" : "PlayerUnknown BattleGround",
#     "number of gamers per team": 4
# }

# # 5) insert document
# first_connection.insert_one(gaem_document)

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