# urllib库 -- python内置的HTTP请求库
# urllib.request -- 请求模块
# urllib.error -- 异常处理模块
# urllib.parse -- url解析模块
# urllib.robotparser -- robots.txt解析模块

# urllib的简单调用 -- get方法
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# urllib -- post
# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# urllib -- get
# import urllib.request
# response = urllib.request.urlopen('http://httpbin.org/get',timeout=1) # timeout指定超时
# print(response.read())

# urllib -- timeout
# import socket
# import urllib.request
# import urllib.error
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

# 响应类型
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(type(response))

# 状态码、响应头
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

