from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get('https://cdn2.byhy.net/files/selenium/test3.html')

element = wd.find_element(By.ID,'input1')
element.send_keys('11333')
sleep(6)
element.clear()

pass