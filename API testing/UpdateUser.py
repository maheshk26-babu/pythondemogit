import requests

payload={
    "name": "morpheus",
    "job": "zion resident"
}
resp = requests.put("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.json())


payload2={
    "name": "API",
}
resp2 = requests.patch("https://reqres.in/api/users/2", data=payload2)
print(resp2)
print(resp2.json())