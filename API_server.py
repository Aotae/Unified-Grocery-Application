import kroger_API # Literally the only api that ended up being half useful
import Safeway_scrape # API wasn't playing nice
import walmart_scrape # No API
import whole_foods_scrape # No API
import UGD_methods

def insert_coupons(id):
    #wrapper for ugd method that uses webscrappers
    for x in id:
        print(x)
        if(x == "Whole Foods"):
            list = whole_foods_scrape.get_items()
            UGD_methods.insert_coupons_collection({"store":x,x+"page":list})
        elif(x == "Walmart"):
            list = walmart_scrape.get_items()
            UGD_methods.insert_coupons_collection({"store":x,x+"page":list})
        elif(x == "Safeway"):
            list = Safeway_scrape.get_items()
            UGD_methods.insert_coupons_collection({"store":x,x+"page":list})

def get_coupon_page(id):
    #wrapper for the ugd method
    couponpage = []
    for x in id:
        if(x == "Whole Foods"):
            page = UGD_methods.get_coupons(x)
            print(page)
            couponpage.append(page)
        elif(x == "Walmart"):
            page = UGD_methods.get_coupons(x)
            print(page)
            couponpage.append(page)
        elif(x == "Safeway"):
            page = UGD_methods.get_coupons(x)
            print(page)
            couponpage.append(page)
    return couponpage

# need seperate function for kroger since it only returns searched items and not their whole catalog.



