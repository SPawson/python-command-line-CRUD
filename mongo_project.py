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

def add_record():
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth in format XX/XX/XXXX > ")
    gender = input("Enter gender > ")
    hair = input("Enter the hair colour > ")
    nationality = input("Enter the nationality > ")
    occupation = input("Enter occupation > ")

    new_doc = {'first': first.lower(), 'last':last.lower(), 'dob':dob.lower(), 'gender': gender.lower(), 'hair_color':hair.lower(), 'nationality':nationality.lower(), 'occupation': occupation.lower()}

    try:
        coll.insert_one(new_doc)
        print("")
        print("Record inserted")
    except:
        print("Error accessing the database")


def main_loop():
    while True:
        option = show_menu()
        #menu options
        if option == "1":
            add_record()
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