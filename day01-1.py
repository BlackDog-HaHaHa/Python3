# 爬虫常用库
# from selenium import webdriver
# driver = webdriver.Chrome() # 操作chrome浏览器
# driver.get('https://www.baidu.com')
# driver.get('https://www.boyisdead.top') # 这个打开就会覆盖掉上次打开的代码
# print(driver.page_source) # 打印页面属性

# from selenium import webdriver
# driver = webdriver.PhantomJS() # 在vscode里执行不成功，在命令行提示成功但提示已被弃用

# from bs4 import BeautifulSoup
# soup = BeautifulSoup('<html></html>','lxml')

# import pymysql
# conn = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='mysql')
# cursor = conn.cursor()
# print(cursor.execute('select * from db'))
# print(cursor.fetchone())

# import pymongo
# client = pymongo.MongoClient('localhost')
# db = client['newtestdb']
# db['table'].insert({'name':'bob'}) # 视频中由于字体问题看起来像元组
# print(db['table'].find_one({'name':'bob'}))

# import redis
# r = redis.Redis('localhost',6379)
# r.set('name','bob')
# print(r.get('name'))

