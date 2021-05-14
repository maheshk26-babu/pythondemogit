import requests

res = requests.get("", timeout=5)
print(res.status_code)