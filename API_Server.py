import requests
#safeway attempts
headers = {
    'Content-Type': 'application/json',
}

data = '{"username":"nathan.ao.pang@gmail.com","password":"124523QweDfgBnm"}'

response = requests.post('https://albertsons.okta.com/api/v1/authn', headers=headers, data=data)
print(response.text +"\n")

headers = {
    'Host': 'albertsons.okta.com',
    'Accept': 'application/json',
    'Authorization': 'Basic bmF0aGFuLmFvLnBhbmdAZ21haWwuY29tOjEyNDUyM1F3ZURmZ0JubQ==',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-us',
    'Content-Type': 'application/x-www-form-urlencoded',
    'charset': 'utf-8',
}

data = 'username=<username>&password=<password>&grant_type=password&scope=openid profile offline_access'

response = requests.post('https://albertsons.okta.com/oauth2/ausp6soxrIyPrm8rS2p6/v1/token', headers=headers, data=data, verify=False)
print(response.text)
#
#kroger attempts
#
