from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Chrome()

# 获取网站
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 根据类class名取值
element = wd.find_elements(By.CLASS_NAME,'animal')

# 取出列表中的每个WebElement对象，打印出其text属性的值
for e in element:
   print(e.text)
   
# find_element 和 find_elements是有区别的，前者范围仅限单个元素，后者范围是所有的相关的元素,
# 且前者选择的是第一个元素，后者是所有元素，如果没有符合条件的元素，前者抛出异常，后者返回一个空列表
   
   
pass