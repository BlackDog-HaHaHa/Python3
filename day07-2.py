# 查找元素

# 单个元素
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q') # 查找q
# input_second = browser.find_element_by_css_selector('#q') # 查找q
# input_third = browser.find_element_by_xpath('//*[@id="q"]') # 查找q
# print(input_first, input_second, input_third)
# browser.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element(By.ID, 'q') # 通用的查找方法
# print(input_first)
# browser.close()


# 多个元素
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_elements_by_css_selector('.service-bd li') # find_elements，返回一个列表
# print(lis)
# browser.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# print(lis)
# browser.close()