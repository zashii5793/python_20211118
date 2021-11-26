import requests
from requests.api import request
rq = requests.get('http://wwww.yahoo.co.jp')
print(rq.text)
print(request)
