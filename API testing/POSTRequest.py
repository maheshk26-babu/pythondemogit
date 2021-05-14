import requests
import json

fp= open("data.json", "r").read()
# print(type(payload))
resp = requests.post("https://reqres.in/api/users", data=json.loads(fp))
print(resp)
assert resp.status_code == 201
print(resp.json())
assert resp.json()['job'] == 'Automation'
print(resp.headers.get('Content_Type'))