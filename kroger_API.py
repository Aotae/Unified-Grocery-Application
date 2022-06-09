import requests
import json


def get_token():
    '''Function to create a new access token to allow the program to access the API'''
    headers = {
        # When done testing hide this api key using .env
        'Authorization': 'Basic Y291cG9udW5pZmllci1jZTViYWVlYWViOWE3ZjU5OTMyNDkwZDlhMDRiZDViOTc5MTgwNTEyNDI1NTI2NDQyNDc6aHIxMnpJQnJ4OV9GTzZGS0hFTnhFbUFERThTZXJmdGVqWnBJbDAzZQ==',
    }

    data = {
        'grant_type': 'client_credentials',
        'scope': 'product.compact',
    }
    #sends a request to the kroger API that sends back a authentication token
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
    #Sends a GET request to the kroger API that sends back product details
    response = requests.get('https://api.kroger.com/v1/products', params=params, headers=headers)


    result = json.loads(response.text)
    return result



