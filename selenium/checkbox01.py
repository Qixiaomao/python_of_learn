from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
wd.implicitly_wait(10)

# checkbox点选框
elements = wd.find_elements(By.CSS_SELECTOR,"#s_checkbox input[checked='checked']")

# 先把已经点击全都点选一遍
for element in elements:
    element.click()
    
# 再点击小雷老师
wd.find_element(By.CSS_SELECTOR,
                "#s_checkbox input[value='小雷老师']").click()

