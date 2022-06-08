import requests
import json
from bs4 import BeautifulSoup

def get_items():
    # these are the stores in Eugene
    urls = ['https://www.coupons.com/coupons/?pid=25351&nid=10&zid=lm54&storezip=97408',
           'https://www.coupons.com/coupons/?pid=25351&nid=10&zid=lm54&storezip=97402']

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        APP_COUPONSINC = soup.find_all('script')[3].text.strip()[21:-1]
        data = json.loads(APP_COUPONSINC)
        return(formatData(data))


def getDictionaryFromJsonData(data):
    bigDict = data.get('contextData')
    for key in bigDict:
        if key == "gallery":
            mediumDict = bigDict.get('gallery')
            for key_2 in mediumDict:
                if key_2 == "podNote":
                    smallDict = mediumDict.get('podCache')
                    #print(smallDict)
                    return smallDict
    return None

def formatData(bigData):
    #print(couponDict)
    couponDict = getDictionaryFromJsonData(bigData)
    allData = []
    for coupon in couponDict:
        newDict = {}
        productInformation = couponDict.get(coupon)
        #print(productInforamation["summary"])
        newDict["summary"] = productInformation["summary"]
        newDict["details"] = productInformation["details"]
        newDict["brand"] = productInformation["brand"]
        newDict["image"] = productInformation["image"]["url"]
        allData.append(newDict)

    return allData
