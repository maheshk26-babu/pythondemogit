import requests

resp= requests.get("", auth=('admin', 'admin'))
print(resp.status_code)