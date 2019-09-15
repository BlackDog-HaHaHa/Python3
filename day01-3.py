from selenium import webdriver
driver = webdriver.Chrome()
# driver.get('https://m.weibo.com')
# driver.get('https://www.zhihu.com')
driver.get('https://www.taobao.com')
print(driver.page_source)