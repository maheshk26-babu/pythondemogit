import requests

resp = requests.delete("https://reqres.in/api/users/2")
# print(resp.status_code)
print(resp.json())
assert resp.status_code == 204, "user deletion failed"