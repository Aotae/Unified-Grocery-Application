import requests
import json


def get_token():
    '''Function to create a new access token to allow the program to access the API'''
    headers = {
        'Authorization': 'Basic Y291cG9udW5pZmllci1jZTViYWVlYWViOWE3ZjU5OTMyNDkwZDlhMDRiZDViOTc5MTgwNTEyNDI1NTI2NDQyNDc6aHIxMnpJQnJ4OV9GTzZGS0hFTnhFbUFERThTZXJmdGVqWnBJbDAzZQ==',
    }

    data = {
        'grant_type': 'client_credentials',
        'scope': 'product.compact',
    }

    response = requests.post('https://api.kroger.com/v1/connect/oauth2/token', headers=headers, data=data)
    result = json.loads(response.text)
    return result["access_token"]

def get_item_detail(item: str, brand: str, token: str):
    '''
    Function that takes in an item name, brand name, and token and returns details about that item.
    '''

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token,
    }

    params = {
        'filter.brand': brand,
        'filter.term': item,
        'filter.locationId': '70100328'
    }

    response = requests.get('https://api.kroger.com/v1/products', params=params, headers=headers)


    result = json.loads(response.text)
    return result


def main():

    token = get_token()

    item = get_item_detail("", "", token)

    return


