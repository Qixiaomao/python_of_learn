# 奇偶数节点
# 选择父元素的偶数节点  nth-child(even)
#  选择父元素的奇数节点  nth-child(odd)
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample1b.html')

# 父元素的奇节点
elements = wd.find_elements(By.CSS_SELECTOR,"p:nth-child(odd)")

for element in elements:
    print('----------')
    print(element.text)