import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def add_coupon_by_id(id, store_id, type):
	headers = {
    'SWY_SSO_TOKEN': '<SWY_SSO_TOKEN> jwt',
    'Content-Type': 'application/json',
	}

	params = (
	    ('storeId', store_id),
	)
	t = Template('{"items":[{"clipType":"C","itemId":"${id}","itemType":"${type}"},{"clipType":"L","itemId":"${id}","itemType":"${type}"}]}')
	data = t.substitute(id=str(id), type=str(type))

	response = requests.post('https://www.safeway.com/abs/pub/web/j4u/api/offers/clip', headers=headers, params=params, data=data)
	print(response.status_code)
##
headers = {
    'Host': 'albertsons.okta.com',
    'Accept': 'application/json',
    'Authorization': 'Basic ',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-us',
    'Content-Type': 'application/x-www-form-urlencoded',
    'charset': 'utf-8',
}

data = 'username=nathan.ao.pang@gmail.com&password=124523QweDfgBnm&grant_type=password&scope=openid profile offline_access'

response = requests.post('https://albertsons.okta.com/oauth2/ausp6soxrIyPrm8rS2p6/v1/token', headers=headers, data=data, verify=False)
print(response.status_code)