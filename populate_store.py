import UGD_methods
import sys
import re
import API_server
"""
Use this script to populate the database with sample data
Written by Nathan Pang
"""
def insert_stores():
    # inserts the 4 stores that we have implemented at the moment.
    UGD_methods.insert_store({"name":"Safeway","coupon_collection_name":"Safeway"})
    UGD_methods.insert_store({"name":"Walmart","coupon_collection_name":"Walmart"})
    UGD_methods.insert_store({"name":"Kroger","coupon_collection_name":"Kroger"})
    UGD_methods.insert_store({"name":"Whole Foods","coupon_collection_name":"Whole Foods"})

def main():
    #formats and calls insert_stores()
    #essentially resets the coupon book
    UGD_methods.delete_stores()
    UGD_methods.delete_coupons_collection()
    insert_stores()
    array = UGD_methods.get_store_library()
    store_list=[]
    for store in array:
        store_name = store["name"]
        store_list.append(store_name)
    #tells the api server to insert coupons
    API_server.insert_coupons(store_list)

main()