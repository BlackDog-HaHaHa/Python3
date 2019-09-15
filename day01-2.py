# import requests
# response = requests.get('https://www.baidu.com')
# print(response) # 这里会返回状态码 <Response [200]>
# print(response.status_code) # 状态码 200
# print(response.text) # 打印源代码
# print(response.headers) # 输出请求头

# import requests
# # head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
# # response = requests.get('https://www.baidu.com', headers=head)
# # print(response.status_code)

# import requests
# response = requests.get('https://www.baidu.com/img/baidu_jgylogo3.gif')
# print(response.content) # 二进制数据流
# with open('./1.gif','wb') as f: # 保存文件
#     f.write(response.content)
#     f.close()
