import requests
#cookies that are used for the request funciton
cookies = {
    'visid_incap_1610353': '9swXCQkaQeusvYOWWCmw6ZsQi2IAAAAAQUIPAAAAAAAhuVaCtX2DV9a89WDoh4n3',
    'aam_uuid': '51750195359134057652755474456465648093',
    'safeway_ga': 'GA1.2.963916370.1653280927',
    '_gcl_au': '1.1.1827622693.1653280927',
    '_pin_unauth': 'dWlkPVpqazVPVGsyTmpFdFpEbGxNQzAwTURjMExXSXlaamd0WmpnMk1XVmtZelEzTm1ReQ',
    '_ga': 'GA1.1.963916370.1653280927',
    'AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg': '1',
    'AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg': '-1124106680%7CMCIDTS%7C19141%7CMCMID%7C55816384279641476813213814359396868985%7CMCAAMLH-1654319279%7C9%7CMCAAMB-1654319279%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1653721679s%7CNONE%7CvVersion%7C5.2.0%7CMCCIDH%7C1175666201',
    'ECommBanner': 'safeway',
    'ECommRedirectURL': '%2Fshop%2Fdeals%2Fmember-specials.html',
    'SAFEWAY_KMSI': 'Error',
    'abs_gsession': '%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D',
    'abs_previouslogin': '%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22houseId%22%3A%22845034582866%22%2C%22clubCard%22%3A%2249540022412%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22isClosed%22%3A%22false%22%2C%22isCrossBannerMFCUser%22%3A%22false%22%2C%22Selection%22%3A%22user%22%2C%22isARenrolled%22%3A%22false%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22address%22%3A%225100%2BBroadway%2C%2BOakland%2C%2BCA%2B94611%22%2C%22preferredBanner%22%3A%22safeway%22%2C%22userData%22%3A%7B%22defaultStore%22%3Afalse%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22address%22%3A%225100%2BBroadway%2C%2BOakland%2C%2BCA%2B94611%22%2C%22userData%22%3A%7B%22guestStoreId%22%3A%223132%22%2C%22guestZipCode%22%3A%2294611%22%2C%22signInCalled%22%3Afalse%2C%22driveUpAndGoIsEnabled%22%3A%22false%22%2C%22unattendedDeliveryIsEnabled%22%3A%22false%22%7D%7D%7D%7D',
    'ECommSignInCount': '0',
    'at_check': 'true',
    'SAFEWAY_MODAL_LINK': '',
    's_vncm': '1654066799745%26vn%3D2',
    's_cc': 'true',
    'safeway_ga_gid': 'GA1.2.837741097.1653714482',
    '_clck': '85uo1h|1|f1u|0',
    '_br_uid_2': 'uid%3D7272369662816%3Av%3D12.0%3Ats%3D1653280926963%3Ahc%3D5',
    '_ga_LZL2CD3SX2': 'GS1.1.1653714511.2.0.1653714511.0',
    's_nr30': '1653714511757-Repeat',
    's_sq': '%5B%5BB%5D%5D',
    '_uetsid': '26a73490de4411ec98641fd5736ef2ca',
    '_uetvid': '1c670040b88d11ecbf7cddf594b5a647',
    '_derived_epik': 'dj0yJnU9dlc1ZzJmRklLRXlvM1k4WUFBZENDclpjT01ScEUwbHombj0xWkhJUDN5U08yYU14SHd4Q2ZJM3l3Jm09ZiZ0PUFBQUFBR0tScmxBJnJtPWYmcnQ9QUFBQUFHS1JybEE',
    'incap_ses_227_1610353': 'A/hNW35RByn7CswIGXgmA0S5kWIAAAAAke+F/nniQhFciTLtp4kzSg==',
    'reese84': '3:+xjL+Z7LSuv+2jehAKoQ7g==:ZNOnOIUpcdXLFLcHKJlzYcl6xVPY/VjMCB1BVDyCOWhVqvPPfxDm94vxWi3ZsM0konv7SYJs8ZjIOZBmdC+JhlKn2WkrWfd2shN4Hj6N6spr+nFJqaLMcmfuG6iaPDJYl/4fCTx36moUcTdBUtJApSM33Gd0o5oqqHXWXJerjG2i+pRs/sVmpJg2yWgKYAXMufDJfgjwQ1pP8BtJPt86iBxYG85XQ6S9ErU+Za5c+of91WMu7BQyXIGc8x3CmET8C29HCIzT+WMSxBg0BzrFEsMD05Blfrk3HqZNJj0Nzq6LR7ehjzFZkNGuS7Xvq6ALKuQAnxOi/7F/o36xvR6OduK5uZZE3x+Sy9WvJYNxPydRHkIXDxjh15HCWS7Yv8YhFP0dLp+xUa5vkR7d5JLMF80AlP+2NYkjajjvBfaXVRnqzC8SavFUCylfOdM/PnkR6eLMpMyIIglulccWNqMgE/NXwaT1QCiAvIyidl6mAOM=:w3I2n8nRfjo7RcjNjwskQBSFJbMybxlxXV65hVabSnU=',
    '_clsk': '1cyje2h|1653718740455|1|0|k.clarity.ms/collect',
    'ADRUM': 's=1653718961203&r=https%3A%2F%2Fwww.safeway.com%2Fforu%2Fcoupons-deals.html',
    'nlbi_1610353': 'hRVJJIY4x0WSar/n6eNT2gAAAADqkBGPI72oYvr/fEHAeVZy',
    'nlbi_1610353_2147483392': '+nqKJHtRKEeq9rhA6eNT2gAAAADdTkJqO3UvtMgXFHBhkgoB',
    'SWY_SHARED_SESSION_INFO': '%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D',
    'SWY_SYND_USER_INFO': '%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D',
    'mbox': 'PC#dfeb827322304e1884e65804ab57f915.35_0#1716963762|session#2eabb405313149eab47701b61c3c6680#1653720822',
}
#headers that are used for the request funcion
headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'adrum': 'isAjax:true',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'visid_incap_1610353=9swXCQkaQeusvYOWWCmw6ZsQi2IAAAAAQUIPAAAAAAAhuVaCtX2DV9a89WDoh4n3; aam_uuid=51750195359134057652755474456465648093; safeway_ga=GA1.2.963916370.1653280927; _gcl_au=1.1.1827622693.1653280927; _pin_unauth=dWlkPVpqazVPVGsyTmpFdFpEbGxNQzAwTURjMExXSXlaamd0WmpnMk1XVmtZelEzTm1ReQ; _ga=GA1.1.963916370.1653280927; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19141%7CMCMID%7C55816384279641476813213814359396868985%7CMCAAMLH-1654319279%7C9%7CMCAAMB-1654319279%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1653721679s%7CNONE%7CvVersion%7C5.2.0%7CMCCIDH%7C1175666201; ECommBanner=safeway; ECommRedirectURL=%2Fshop%2Fdeals%2Fmember-specials.html; SAFEWAY_KMSI=Error; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22houseId%22%3A%22845034582866%22%2C%22clubCard%22%3A%2249540022412%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22isClosed%22%3A%22false%22%2C%22isCrossBannerMFCUser%22%3A%22false%22%2C%22Selection%22%3A%22user%22%2C%22isARenrolled%22%3A%22false%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22address%22%3A%225100%2BBroadway%2C%2BOakland%2C%2BCA%2B94611%22%2C%22preferredBanner%22%3A%22safeway%22%2C%22userData%22%3A%7B%22defaultStore%22%3Afalse%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22address%22%3A%225100%2BBroadway%2C%2BOakland%2C%2BCA%2B94611%22%2C%22userData%22%3A%7B%22guestStoreId%22%3A%223132%22%2C%22guestZipCode%22%3A%2294611%22%2C%22signInCalled%22%3Afalse%2C%22driveUpAndGoIsEnabled%22%3A%22false%22%2C%22unattendedDeliveryIsEnabled%22%3A%22false%22%7D%7D%7D%7D; ECommSignInCount=0; at_check=true; SAFEWAY_MODAL_LINK=; s_vncm=1654066799745%26vn%3D2; s_cc=true; safeway_ga_gid=GA1.2.837741097.1653714482; _clck=85uo1h|1|f1u|0; _br_uid_2=uid%3D7272369662816%3Av%3D12.0%3Ats%3D1653280926963%3Ahc%3D5; _ga_LZL2CD3SX2=GS1.1.1653714511.2.0.1653714511.0; s_nr30=1653714511757-Repeat; s_sq=%5B%5BB%5D%5D; _uetsid=26a73490de4411ec98641fd5736ef2ca; _uetvid=1c670040b88d11ecbf7cddf594b5a647; _derived_epik=dj0yJnU9dlc1ZzJmRklLRXlvM1k4WUFBZENDclpjT01ScEUwbHombj0xWkhJUDN5U08yYU14SHd4Q2ZJM3l3Jm09ZiZ0PUFBQUFBR0tScmxBJnJtPWYmcnQ9QUFBQUFHS1JybEE; incap_ses_227_1610353=A/hNW35RByn7CswIGXgmA0S5kWIAAAAAke+F/nniQhFciTLtp4kzSg==; reese84=3:+xjL+Z7LSuv+2jehAKoQ7g==:ZNOnOIUpcdXLFLcHKJlzYcl6xVPY/VjMCB1BVDyCOWhVqvPPfxDm94vxWi3ZsM0konv7SYJs8ZjIOZBmdC+JhlKn2WkrWfd2shN4Hj6N6spr+nFJqaLMcmfuG6iaPDJYl/4fCTx36moUcTdBUtJApSM33Gd0o5oqqHXWXJerjG2i+pRs/sVmpJg2yWgKYAXMufDJfgjwQ1pP8BtJPt86iBxYG85XQ6S9ErU+Za5c+of91WMu7BQyXIGc8x3CmET8C29HCIzT+WMSxBg0BzrFEsMD05Blfrk3HqZNJj0Nzq6LR7ehjzFZkNGuS7Xvq6ALKuQAnxOi/7F/o36xvR6OduK5uZZE3x+Sy9WvJYNxPydRHkIXDxjh15HCWS7Yv8YhFP0dLp+xUa5vkR7d5JLMF80AlP+2NYkjajjvBfaXVRnqzC8SavFUCylfOdM/PnkR6eLMpMyIIglulccWNqMgE/NXwaT1QCiAvIyidl6mAOM=:w3I2n8nRfjo7RcjNjwskQBSFJbMybxlxXV65hVabSnU=; _clsk=1cyje2h|1653718740455|1|0|k.clarity.ms/collect; ADRUM=s=1653718961203&r=https%3A%2F%2Fwww.safeway.com%2Fshop%2Fdeals%2Fmember-specials.html; nlbi_1610353=hRVJJIY4x0WSar/n6eNT2gAAAADqkBGPI72oYvr/fEHAeVZy; nlbi_1610353_2147483392=+nqKJHtRKEeq9rhA6eNT2gAAAADdTkJqO3UvtMgXFHBhkgoB; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D; mbox=PC#dfeb827322304e1884e65804ab57f915.35_0#1716963762|session#2eabb405313149eab47701b61c3c6680#1653720822',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/foru/coupons-deals.html',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
}

#response contains all items in the deals section of Safeway in a JSON format
#Use this function to get product details from Safeway
def get_items():
    response = requests.get('https://www.safeway.com/abs/pub/xapi/search/products?request-id=8218844936810&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=search&rows=30&start=0&search-type=keyword&storeid=3132&featured=false&search-uid=uid%253D7272369662816%253Av%253D12.0%253Ats%253D1653280926963%253Ahc%253D5&q=&sort=&userid=&featuredsessionid=&screenwidth=1283&channel=instore&banner=safeway&fq=promoType:%22P%22&fq=inventoryAvailable:%221%22', cookies=cookies, headers=headers)
    return response.json()
#USED FOR TESTING
def main():
    a = get_items()
    a = a['response']
    a = a['docs']
    print(a)

#main()
