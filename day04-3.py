# 已过期
import requests
import re

content = requests.get("https://book.douban.com/").text
# print(content)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
result = re.findall(pattern,content)
print(result)
