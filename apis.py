import os
from PIL import Image
from IPython.display import IFrame
import requests
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
r= requests.get(url)
print(r.status_code)
print(r.request.body)

header = r.headers
print(header['Content-Type'])
with open("ibm.txt", 'w') as file:
    file.write(r.text[0:])

url_get = 'http:httpbin.org/get'
payload = {"name":"Joseph","ID":"123"}
r = requests.get(url_get, params=payload)

print(r.url)
