import UGD_methods
import sys
import re
"""
Use this script to populate the database with sample data
Written by Nathan Pang
"""
def insert_library():
    UGD_methods.insert_store({"name":"Safeway","coupon_collection_name":"Safeway"})
    UGD_methods.insert_store({"name":"Walmart","coupon_collection_name":"Walmart"})
    UGD_methods.insert_store({"name":"Kroger","coupon_collection_name":"Kroger"})
    UGD_methods.insert_store({"name":"Whole Foods","coupon_collection_name":"Whole Foods"})

def main():
    file = open(sys.argv[1],'r',errors='ignore')
    Lines = file.readlines()
    print(Lines)
    #insert_library()
    content = ""
    for line in Lines:
        content += line
    UUGD_methods.insert_stores({"name":Lines[0],"coupon_collection_name":Lines[1]})

#MDBClient.delete_library()
#MDBClient.delete_note_library()
#main()
UGD_methods.delete_stores();
insert_library();