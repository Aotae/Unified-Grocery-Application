import requests
cookies = {
    'csm-sid': '637-1450553-2361065',
    '_gcl_au': '1.1.68708868.1654017178',
    'session-id': '139-0115561-4142474',
    'session-id-time': '2082787201l',
    '_ga': 'GA1.2.1674474337.1654017179',
    '_gid': 'GA1.2.223950669.1654017179',
    'ubid-main': '130-3996490-5069637',
    'session-token': 'bOEqIOr6wjhn5IhrvYL1zdCn1UuI0d6eyXuk6oC5refM/aHdlQi0lGAeFdCsqM3R8TW2+6ujf0OBLgNG+e9L9axG6cJhjg7BUmUuAPglMlHkrwNt8TnrsYHhHP76ONN1wx9CRaaFXRJYTzgS2xxM9znv7uQKI5jYJs/rFJhiZ2wY9YMzEzKOyfyLGhFCPefX',
    'wfm_store_weak': 'eyJ2ZXJzaW9uIjoxLCJzdG9yZUlkIjoxMDI5NCwiZ2VvQ29vcmRpbmF0ZSI6eyJsYXRpdHVkZSI6NDQuMDUwMTExLCJsb25naXR1ZGUiOi0xMjMuMDg3ODYzLCJhbHRpdHVkZU1ldGVycyI6MC4wfX0',
    'wfm_store_d8': 'eyJpZCI6IjEwMjk0IiwibmFtZSI6IkV1Z2VuZSIsInRsYyI6IkVVRyIsInBhdGgiOiJldWdlbmUiLCJzdGF0ZSI6Ik9SIiwic3RvcmVfbmlkIjoiIiwic3RhcnRfZGF0ZSI6IjIwMjItMDUtMzFUMTc6MTU6MjkuMDk5WiIsInVwZGF0ZWRfZGF0ZSI6IjIwMjItMDUtMzFUMTc6MTU6MjkuMDk5WiIsImdlb21ldHJ5Ijp7ImNvb3JkaW5hdGVzIjpbLTEyMy4wODc4NjMsNDQuMDUwMTExXSwidHlwZSI6IlBvaW50In19',
    '_gat_UA-190385-1': '1',
}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'csm-sid=637-1450553-2361065; _gcl_au=1.1.68708868.1654017178; session-id=139-0115561-4142474; session-id-time=2082787201l; _ga=GA1.2.1674474337.1654017179; _gid=GA1.2.223950669.1654017179; ubid-main=130-3996490-5069637; session-token=bOEqIOr6wjhn5IhrvYL1zdCn1UuI0d6eyXuk6oC5refM/aHdlQi0lGAeFdCsqM3R8TW2+6ujf0OBLgNG+e9L9axG6cJhjg7BUmUuAPglMlHkrwNt8TnrsYHhHP76ONN1wx9CRaaFXRJYTzgS2xxM9znv7uQKI5jYJs/rFJhiZ2wY9YMzEzKOyfyLGhFCPefX; wfm_store_weak=eyJ2ZXJzaW9uIjoxLCJzdG9yZUlkIjoxMDI5NCwiZ2VvQ29vcmRpbmF0ZSI6eyJsYXRpdHVkZSI6NDQuMDUwMTExLCJsb25naXR1ZGUiOi0xMjMuMDg3ODYzLCJhbHRpdHVkZU1ldGVycyI6MC4wfX0; wfm_store_d8=eyJpZCI6IjEwMjk0IiwibmFtZSI6IkV1Z2VuZSIsInRsYyI6IkVVRyIsInBhdGgiOiJldWdlbmUiLCJzdGF0ZSI6Ik9SIiwic3RvcmVfbmlkIjoiIiwic3RhcnRfZGF0ZSI6IjIwMjItMDUtMzFUMTc6MTU6MjkuMDk5WiIsInVwZGF0ZWRfZGF0ZSI6IjIwMjItMDUtMzFUMTc6MTU6MjkuMDk5WiIsImdlb21ldHJ5Ijp7ImNvb3JkaW5hdGVzIjpbLTEyMy4wODc4NjMsNDQuMDUwMTExXSwidHlwZSI6IlBvaW50In19; _gat_UA-190385-1=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
params = {
    'featured': 'on-sale',
    'store': '10294',
    'category': 'all-products',
}
def get_items():
    response = requests.get('https://www.wholefoodsmarket.com/_next/data/TUm8mEYAFTdEvI3m8dk80/products/all-products.json', params=params, cookies=cookies, headers=headers)
    return response.json()
