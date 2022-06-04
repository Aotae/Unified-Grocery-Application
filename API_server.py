import kroger_API # Literally the only api that ended up being half useful
import Safeway_scrape # API wasn't playing nice
import walmart_scrape # No API
import whole_foods_scrape # No API
import UGD_methods

def insert_coupons(id):
    #wrapper for ugd method that uses webscrappers
    for x in id:
        if(x == "Whole Foods"):
            list = whole_foods_scrape.get_items()
            UGD_methods.insert_coupons_collection({x:list})
        elif(x == "Walmart"):
            list = walmart_scrape.get_items()
            UGD_methods.insert_coupons_collection({x:list})
        elif(x == "Safeway"):
            list = Safeway_scrape.get_items()
            UGD_methods.insert_coupons_collection({x:list})

def get_coupon_page(id):
    #wrapper for the ugd method
    couponpage = []
    for x in id:
        if(x == "Whole Foods"):
            couponpage.append(UGD_methods.get_coupons(x))
        elif(x == "Walmart"):
            couponpage.append(UGD_methods.get_coupons(x))
        elif(x == "Safeway"):
            couponpage.append(UGD_methods.get_coupons(x))
    return couponpage

# need seperate function for kroger since it only returns searched items and not their whole catalog.



