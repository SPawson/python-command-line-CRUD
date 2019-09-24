import pymongo
import os

MONGODB_URI = os.getenv('MONGO_URI') # gets windows enviroment var value
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Connected")
        return conn # returns connection object
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI) #returns object into conn var

coll = conn[DBS_NAME][COLLECTION_NAME] #accessing the test db from the conn object, saving in coll var

# new_doc = {'first': 'douglas','last':'adams', 'dob': '11/03/1952',
# 'hair_colour':'grey','occupation':'writer','nationality':'english'}

# new_docs = [{'first': 'terry','last':'pratchet', 'dob': '28/04/1948', 'gender':'m',
# 'hair_colour':'not much','occupation':'writer','nationality':'english'},{'first': 'george','last':'rr martin', 'dob': '20/09/1948', 'gender':'m',
# 'hair_colour':'white','occupation':'writer','nationality':'american'}]

# #coll.insert_one(new_doc)

# coll.insert_many(new_docs)

#documents = coll.find({'first':'douglas'}) #calling the find command on the object - use dictionary for key value pair

#coll.delete_one({'first':'douglas'}) # will remove record with given search term i.e key value pair

#coll.update_one({'nationality':'american'}, {'$set': {'hair_colour':'maroon'}}) #update one will only change first record

coll.update_many({'nationality':'american'}, {'$set': {'hair_colour':'brown'}})


documents = coll.find({'nationality':'american'})

for doc in documents:
    print(doc)

