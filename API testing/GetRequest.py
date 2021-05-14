import requests

resp= requests.get("https://reqres.in/api/users?page=2")
code= resp.status_code
assert code == 200, "response code doesnt match"

print(resp.text)
print(resp.content)
print(resp.json())
print(resp.headers)
print(resp.cookies)
print(resp.encoding)
print(resp.url)