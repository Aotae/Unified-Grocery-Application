import pymongo
import mongoengine

from pymongo import MongoClient
"""
Database functions for the Unified Grocery Store Database.
"""

#connects to the mongodb database and checks to see if its valid.
def connect():
    #for now just local
    client = pymongo.MongoClient("mongodb://localhost:27017")
    if not client:
        raise Exception('bad connection with db')
    return client

def insert_user(user):
    # inserts one document into the 'note-library' collection
    # a document includes a User's Username and Password.
    # POST request 
    client = connect()
    db = client["UGD"]
    collection = db["Users"]
    collection.insert_one(user)

def update(id,value):
    # Updates a document found with id with value i.e {user:username, password:hashed} for if the user forgets their password.
    # PUT request
    client = connect()
    db = client["UGD"]
    collection = db["Users"]
    collection.update_one(id,{"$set":value})

def insert_store(store):
    # inserts one document i.e book into the 'library' collection
    # a document includes information on a book such as title and author as well as a cover image
    # a document is a dictionary in this form {store:grocery store name, coupon_pointer:grocery store coupon pointer}
    # POST request
    client = connect()
    db = client["UGD"]
    collection = db["GroceryStores"]
    collection.insert_one(store)

def delete_store(id):
    # deletes one document i.e book from the 'GroceryStores' collection
    # locates book using id, id should be formatted as a query {store:grocery store name} since we use book names as our book ids
    # DELETE request
    client = connect()
    db = client["UGD"]
    collection = db["GroceryStores"]
    collection.delete_one(id)

def delete_stores():
    # Drops the collection 'GroceryStores'
    # DELETE request
    client = connect()
    db = client["UGD"]
    collection = db["GroceryStores"]
    collection.drop()

def get_user_password(id):
    # gets the notes from the 'note-library' collection according to bookname(id)
    # id should be formatted {User:Username} as we use usernames as our ids
    # GET request
    client = connect()
    db = client["UGD"]
    collection = db["Users"]
    return collection.find_one(id)

def get_store(id):
    # gets a store from the 'GroceryStores' collection according to store name(id)
    # id should be formatted {store:storename} as we use booknames as our book ids
    # GET request
    client = connect()
    db = client["UGD"]
    collection = db["GroceryStores"]
    return collection.find_one(id)

def get_store_library():
     # returns all of the documents in the 'GroceryStores' collection
    collection_array = []
    client = connect()
    db = client["UGD"]
    collection = db["GroceryStores"]
    cursor = collection.find({})
    for document in cursor:
        collection_array.append(document)
    return collection_array

def User_exists(id):
    # checks if notes for a certain user exist
    client = connect()
    db = client["UGD"]
    collection = db["Users"]
    count = collection.count_documents(id)
    if(count>0):
        return True
    else:
        return False

def get_coupons(store_id):
    client = connect()
    db = client["UGD"]
    collection = db["Coupon"]
    return collection.find_one(id)
def insert_coupons_collection(couponPage):
    # Document should be formatted s.t {store:storename, coupon:couponobject[]}
    client = connect()
    db = client["UGD"]
    collection = db["Coupon"]
    collection.insert_one(couponPage)
def delete_user_collection():
    # FOR TESTING PURPOSES HAS NO USE IN DEPLOYMENT UNLESS YOU WANT TO GET RID OF ALL OF YOUR POTENTIAL USERS
    # WILL DROP ALL OF THE NOTES ASSOCIATED WITH ALL BOOKS
    client = connect()
    db = client["UGD"]
    collection = db["Users"]
    collection.drop()
def delete_coupons_collection():
    # Document should be formatted s.t {store:storename, coupon:couponobject[]}
    client = connect()
    db = client["UGD"]
    collection = db["Coupon"]
    collection.drop()