from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

db_demo = client.get_database()

a = db_demo["posts"]
b = db_demo["customers"]
customers= b.find()

post_document = {
    "title" : "Chủ tịch techkids thử lòng học viên và cái kết ",
    "author" : "QQT School",
    "content": 
    "Tịch cái đcm j suốt ngày tịch \n Dăm ba tk rảnh háng đi thử lòng người khác?? \nChủ tịch mà rảnh như chg m thì công ty nát cmnr :) \n Btw, bố m là chủ tịch techkids đây :)"
}

a.insert_one(post_document)
ref_list=[]
checked=[]
ref_count=[]
for customer in customers:
    ref_list.append(customer["ref"])
for ref in ref_list:
    while True:
        if ref in checked:
            break
        else :
            ref_count.append(ref_list.count(ref))
            checked.append(ref)

pyplot.pie(ref_count, labels =checked, autopct="%.1f%%", shadow=True, explode=[0,0.2,0.1])
pyplot.axis('equal')
pyplot.title("REFERENCE RATE")
pyplot.show() 

a.update_one({"title":"09"},{ "$set" :{"author":"đạt xả lín","content":"dăm ba tk gửi bài sớm :))"}})
