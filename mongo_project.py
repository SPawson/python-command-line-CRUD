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
    """Displays the text menu to the user"""

    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter an option > ")
    return option

conn = mongo_connect(MONGODB_URI) #returns object into conn var

coll = conn[DBS_NAME][COLLECTION_NAME]

def get_record():
    print("")
    first = input("Enter first name > ") #first name of record
    last = input("Enter last name > ") # lastname of record to be searched

    record = {'first': first.lower(), 'last': last.lower()} #combines names into same var

    try:
        doc = coll.find_one(record) #Searches database for the record
    except:
        print("Error accessing database")
    
    if not doc: # If doc doesnt contain any items it will notify the user
        print("")
        print("Error! No results found for %s %s" % (first.lower(), last.lower()))

    return doc

def add_record():
    """This will ask for all input fields to be entered then will submit to the DB"""

    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth in format XX/XX/XXXX > ")
    gender = input("Enter gender > ")
    hair = input("Enter the hair colour > ")
    nationality = input("Enter the nationality > ")
    occupation = input("Enter occupation > ")

    new_doc = {'first': first.lower(), 'last':last.lower(), 'dob':dob.lower(), 'gender': gender.lower(), 'hair_color':hair.lower(), 'nationality':nationality.lower(), 'occupation': occupation.lower()}

    try:
        coll.insert_one(new_doc) # calls insert method and submits the record
        print("")
        print("Record inserted")
    except:
        print("Error accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items(): #items method will display k,v in doc var
            if k != "_id": #If key doesnt equal the id then it wont be printed
                print(k.upper() + ": " + v.upper())

def edit_record():
    doc = get_record()

    if doc:
        update_doc = {}
        print("")
        for k,v in doc.items():
            if k != "_id": 
                update_doc[k] = input(k.upper() + " [" + v + "] > ") # enters the value for the current key

                if update_doc[k] == "":
                    update_doc[k] = v #if doc is left blank it puts current value in record

        try:
            #print(update_doc)
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Record updated")
        except:
            print("Error accessing database")

def main_loop():
    """Main loop of the program runs from here """

    while True:
        option = show_menu()
        #menu options
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            print('You have selected option 4')
        elif option == "5":
            print('Goodbye')
            conn.close()
            break
        else:
            print("Please enter a valid choice")

main_loop() # Main loop called and activated