from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

element = wd.find_element(By.CSS_SELECTOR,"[href]")

print(element.get_attribute('outerHTML'))
