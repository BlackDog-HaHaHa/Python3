# import requests
# response = requests.get('http://www.baidu.com')
# print(type(response.text))
# print(response.cookies)

# get请求
# import requests
# response = requests.get('http://httpbin.org/get')
# print(response.text)

# 带参数的get请求
# import requests
# response = requests.get("http://httpbin.org/get?name=germey&age=22")
# print(response.text)

# 字典传参
# import requests
# data = {
#     'name':'germey',
#     'age':22
# }
# response = requests.get("http://httpbin.org/get",params=data)
# print(response.text)

# 关于params
# 你也许经常想为 URL 的查询字符串(query string)传递某种数据。
# 如果你是手工构建 URL，那么数据会以键/值对的形式置于 URL 中，跟在一个问号的后面。
# 例如， httpbin.org/get?key=val。 Requests 允许你使用 params 关键字参数，以一个字符串字典来提供这些参数。
# 举例来说，如果你想传递 key1=value1 和 key2=value2 到 httpbin.org/get ，那么你可以使用如下代码：
# >>> payload = {'key1': 'value1', 'key2': 'value2'}
# >>> r = requests.get("http://httpbin.org/get", params=payload)

# 获取二进制数据
# import requests
# response = requests.get("https://github.com/favicon.ico")
# print(type(response.text),type(response.content))
# print(response.text)
# print(response.content)

# 将获取到的图片保存
# import requests
# response = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico','wb') as f:
#     f.write(response.content)
#     f.close()

# headers
# import requests
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
# }
# response = requests.get("http://httpbin.org/headers",headers=headers)
# print(response.text)

# import requests
# response = requests.get("http://www.baidu.com")
# print(response.status_code,type(response.status_code))
# print(response.headers,type(response.headers))
# print(response.cookies,type(response.cookies))
# print(response.url,type(response.url))
# print(response.history,type(response.history))
# 默认情况下，除了 HEAD, Requests 会自动处理所有重定向。
# 可以使用响应对象的 history 方法来追踪重定向。
# Response.history 是一个 Response 对象的列表，为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的请求进行排序。

# status code
# import requests
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
# }
# response = requests.get("http://www.jianshu.com/hello.html",headers=headers)
# print(response.status_code)
# # exit() if not response.status_code == requests.codes.not_found else print("404 not found")
# exit() if not response.status_code == 404 else print("404 not found")

# post提交
# import requests
# files = {'file':open('favicon.ico','rb')}
# response = requests.post("http://httpbin.org/post",files=files)
# print(response.text)

# get cookie
# import requests
# response = requests.get("https://www.baidu.com")
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key + '=' + value)

# 会话维持
# import requests
# requests.get("http://httpbin.org/cookie/set/number/123456789")
# response = requests.get("http://httpbin.org/cookies")
# print(response.text)

# import requests
# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
# response = s.get("http://httpbin.org/cookies")
# print(response.text)
# 与上面那种方法不同的是，第一种不会返回我们传入的cookie值
# 因为第一种方法实际上相当于在两个独立的浏览器里访问，cookie是不会共享的
# 第二种方法是创建了一个session，因此返回了cookie值

# 证书验证
# import requests
# response = requests.get('https://www.12306.cn')
# print(response.status_code)

# import requests
# response = requests.get('https://www.12306.cn',verify=False) # verify参数用来关闭https证书验证，但这样就会报警告
# print(response.status_code)

# import requests
# response = requests.get("https://www.12306.cn",cert=('/path/server.crt','/path/key'))
# print(response.status_code)
# 通过添加一个证书来消除警告