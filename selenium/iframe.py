#iframe切换窗口
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')

# 切换窗口
wd.switch_to.frame('frame1')

# 根据class name 选择元素 返回的是一个列表
elements = wd.find_elements(By.CLASS_NAME,'plant')

for element in elements:
    print(element.text)
    
# 如果又要切换到原html页面
# wd.switch_to.default_content()

wd.switch_to.default_content()
# 再次选择操作外部的 HTML中的元素
wd.find_element(By.ID,"outerbutton").click()



sleep(4)

wd.quit()

