import requests

p = {"page": 2}
resp= requests.get("https://reqres.in/api/users", params=p)
print(resp.url)
json_repsonse = resp.json()
print(json_repsonse['total'])
assert json_repsonse['total']==12
print(json_repsonse['total_pages'])
assert json_repsonse['total_pages']==2, "Total pages count is not matching"
print(json_repsonse['data'][0]['email'])
assert (json_repsonse['data'][0]['email']).endswith("reqres.in"), "email id is not matching"
print(json_repsonse['data'][2]['last_name'])
assert (json_repsonse['data'][2]['last_name']) != None
print(json_repsonse['support']['url'])