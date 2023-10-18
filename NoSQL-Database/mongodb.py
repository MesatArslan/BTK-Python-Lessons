import pymongo
from bson.objectid import ObjectId


################ Mongodb connections ##############

# myclient = pymongo.MongoClient("mongodb://localhost")
myclient = pymongo.MongoClient("mongodb+srv://justlearnfrom2002:iSMAS2RjQfCj6TB4@cluster0.umnqlzc.mongodb.net/")

mydb = myclient["node-app"]
# print(myclient.list_database_names())




############### Creating collections ############

mycollection = mydb["products"]
# print(mydb.list_collection_names())


# product = {"name":"Samsung S8", "price":2000}

# result = mycollection.insert_one(product)
# print(result)
# print(type(result))
# # print(result.inserted_id) # object id yi görürüz

# productlist = [
#     {"name":"Samsung S11", "price":3000, "description":"Goog Phone"},
#     {"name":"Samsung S12", "price":4000,"categories":["Phone","Electronic"]},
#     # {"id":1,"name":"Samsung S11", "price":3000},
#     # {"id":2,"name":"Samsung S12", "price":4000},
#     {"name":"Samsung S13", "price":5000},
#     {"name":"Samsung S14", "price":6000},
#     {"name":"Samsung S15", "price":7000},
#     {"name":"Samsung S16", "price":8000}
# ]
# result = mycollection.insert_many(productlist)
# print(result.inserted_ids)




############ Find Records ############

# result = mycollection.find_one()
# for i in mycollection.find():
# for i in mycollection.find({},{"_id":0,"name":1,"price":1}):
# for i in mycollection.find({},{"_id":0}):
# for i in mycollection.find({},{"name":1}):
#     print(i)
# print(result)




############ Filtering ############

filter = {"name":"Samsung S8", "price":2000}


# result =mycollection.find({"name":"Samsung S8", "price":2000})
# result =mycollection.find_one(filter)
# result = mycollection.find_one({"_id": ObjectId("652f8164197ace9bdd4c7feb")})
# result =mycollection.find(filter)

# result = mycollection.find({
#     "name": {
#         "$in":["SAmsung S8","Samsung S12"]
        
#     }
# })

# result = mycollection.find({
#     "price":{
#         # "$gt": 5000
#         "$gte": 5000
#     }
# })

# result = mycollection.find({
#     "price":{
#         "$eq": 5000
#     }
# })

# result = mycollection.find({
#     "name": {
#         "$regex": "^S"
#     }
# })

# for i in result:
#     print(i)




############ Sorting ############

# result = mycollection.find().sort("name")
# result = mycollection.find().sort("name",1)
# result = mycollection.find().sort("name",-1)

# result = mycollection.find().sort("price")
# result = mycollection.find().sort("price",1)
# result = mycollection.find().sort("price",-1)

# result = mycollection.find().sort([("name",1),("price",-1)])

# for i in result:
#     print(i)




############ Updating ############

# for i in mycollection.find():
#     print(i)

# mycollection.update_one(
#     {"name":"Samsung S8"},
#     {"$set": {
#         "name": "IPhone 10",
#         "price": "30000"
#     }}    
# )

# mycollection.update_one(
#     {"name":"Samsung S12"},
#     {"$set": {
#         "name": "IPhone 13",
#         "price": "60000"
#     }}    
# )

# mycollection.update_many(
#     {"name":"Samsung S13"},
#     {"$set": {
#         "name": "IPhone 11",
#         "price": "60000"
#     }}    
# )

# query = {"name":"Samsung S13"}

# newValues = {"$set": {
#         "name": "IPhone 11",
#         "price": "60000"
#     }}    
# result = mycollection.update_many(query, newValues)

# print(f'{result.modified_count} records updated.')

# for i in mycollection.find():
#     print(i)




############ Deleting ############

for i in mycollection.find():
    print(i)

print('*'*50)

# mycollection.delete_one({"name":"Samsung S14"})
mycollection.delete_many({"name":"Samsung S14"})
mycollection.delete_many({"name":{"$regex":"^S"}})
result =mycollection.delete_many({})

print(f'{result.deleted_count} records deleted')

for i in mycollection.find():
    print(i)