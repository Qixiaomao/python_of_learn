# radio框选择
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
wd.implicitly_wait(10)


element = wd.find_element(By.CSS_SELECTOR,"#s_radio input[checked=checked]")
print(f"当前选中的是：{element.get_attribute('value')}")

# 点选 小雷老师
wd.find_element(By.CSS_SELECTOR,"#s_radio input[value='小雷老师']").click()


