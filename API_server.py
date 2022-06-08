import kroger_API # Literally the only api that ended up being half useful
import Safeway_scrape # couldn't back engineer their API since we didn't have a way to perform a 
                      # man in the middle attack to get the way they make JWTs
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
    print(id)
    if(not id):
        array = UGD_methods.get_store_library()
        store_list=[]
        for store in array:
            store_name = store["name"]
            store_list.append(store_name)
        id = store_list
    #print(id)
    page = get_coupon_page(id)
    if(keyword == None):
        return page
    searchlist = []
    for x in page:
        #print(x)
        for i in x:
            try:
                key_item_name = i['name']
                namestore = 1
                print(key_item_name + " name")
            except:
                key_item_name = i['details']
                couponinfo = {"details":key_item_name,"promo":i["summary"],"image":i['image']}
                namestore = 0
                print(key_item_name + " details")
            if(namestore == 1):
                try:
                    price = i['promoDescription']
                    couponinfo = {"details":key_item_name,"promo":price}
                except:
                    fullprice = i['regularPrice']
                    price = i['salePrice']
                    couponinfo = {"details":key_item_name,"promo":[price,fullprice],"image":i['imageThumbnail']}
            if(keyword.lower() in key_item_name.lower() or keyword.lower()[:-1] in key_item_name.lower()):
                searchlist.append(couponinfo)

    if("Kroger" in id):
        token = kroger_API.get_token()
        a = kroger_API.get_item_detail(keyword,"",token)
        searchlist.append(a)
    print(searchlist)
    return searchlist


