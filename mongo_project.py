import pymongo
import os

MONGODB_URI = os.getenv('MONGO_URI') # gets windows enviroment var value
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn # returns connection object
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter an option")
    return option

conn = mongo_connect(MONGODB_URI) #returns object into conn var

coll = conn[DBS_NAME][COLLECTION_NAME]

def main_loop():
    while True:
        option = show_menu()

        if option == "1":
            print('You have selected option 1')
        elif option == "2":
            print('You have selected option 2')
        elif option == "3":
            print('You have selected option 3')
        elif option == "4":
            print('You have selected option 4')
        elif option == "5":
            print('Goodbye')
            conn.close()
            break
        else:
            print("Please enter a valid choice")

main_loop()