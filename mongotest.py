import pymongo

client = pymongo.MongoClient("mongodb+srv://dipaksutar123:Sutar264128@cluster0.ustl2.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)


d={
    "name":"dipak",
    "email":"dipaksutar123@gmail.com",
    "surname":"sutar"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)