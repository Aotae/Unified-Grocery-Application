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
            a = page[f"{x}page"]
            a = a['pageProps']
            a = a['data']
            a = a['results']
            #print(a)
            couponpage.append(a)
        elif(x == "Walmart"):
            page = UGD_methods.get_coupons(x)
            a = page[f"{x}page"]
            #print(a)
            couponpage.append(a)
        elif(x == "Safeway"):
            
            page = UGD_methods.get_coupons(x)
            a = page[f"{x}page"]
            a = a['response']
            a = a['docs']
            #print(a)
            couponpage.append(a)
    return couponpage

def search_coupon_page(id,keyword):
    if(id == None):
        array = UGD_methods.get_store_library()
        store_list=[]
        for store in array:
            store_name = store["name"]
            store_list.append(store_name)
        id = store_list
    page = get_coupon_page(id)
    if(keyword == None):
        return page
    searchlist = []
    for x in page:
        #print(x)
        for i in x:
            try:
                key = i['name']
            except:
                key = i['details']
            print(key)
            if(keyword in key):
                searchlist.append(i)
    if("Kroger" in id):
        token = kroger_API.get_token()
        a = kroger_API.get_item_detail(keyword,"",token)
        searchlist.append(a)
    print(searchlist)
    return searchlist
                

# need seperate function for kroger since it only returns searched items and not their whole catalog.



