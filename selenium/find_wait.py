from selenium import webdriver
from selenium.webdriver.common.by import By

# 设置该浏览器对象
wd = webdriver.Chrome() 
# implicitly_wait函数,当页面没有获取到动态数据时，就再次请求页面，直到超出给定的限定值
wd.implicitly_wait(10)

wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID,'kw')

element.send_keys('通讯\n')

# 返回页面ID为1的元素
element = wd.find_element(By.ID,'1')

print(element.text)

