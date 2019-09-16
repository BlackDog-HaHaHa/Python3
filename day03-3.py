# 超时
import requests
from requests.exceptions import ConnectTimeout
try:
    response = requests.get("http://www.baidu.com", timeout=0.01)
    print(response.status_code)
except ConnectTimeout:
    print("timeout")