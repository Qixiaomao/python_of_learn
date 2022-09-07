# 对于元素的操作
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://www.baidu.com/')

from selenium.webdriver.common.action_chains import ActionChains

ac = ActionChains(wd)

# 鼠标移动到 元素上
ac.move_to_element(
    wd.find_element(By.CSS_SELECTOR,'[name="tj_briicon"]')
).perform()