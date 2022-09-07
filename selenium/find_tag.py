'''根据tag名选择元素'''

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 根据tag name 选择元素，返回的是一个列表
elements = wd.find_elements(By.TAG_NAME,'div')

# 取出该列表元素并打印出来
for element in elements:
    print(element.text)