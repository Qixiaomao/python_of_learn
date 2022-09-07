# 绝对路径使用
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://cdn2.byhy.net/files/selenium/test1.html")

element = wd.find_element(By.XPATH,'//*[@id="newyork"]')

print(element.text)

