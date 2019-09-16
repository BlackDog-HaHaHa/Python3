# 认证
import requests
from requests.auth import HTTPBasicAuth
# r = requests.get("http://192.168.123.1",auth=HTTPBasicAuth('admin','admin'))
r = requests.get("http://192.168.123.1",auth=('admin','admin')) # 两种写法都可以的
print(r.status_code)