# 父元素的第n个子节点
# 如果要选择父元素里一排子元素的某个子节点
# 语法就是nth-child
# 父元素里的第n个子节点
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample1b.html')

# 父元素的第n个子节点
# elements = wd.find_elements(By.CSS_SELECTOR,"#t1 span:nth-child(2) ,#t2 span:nth-child(2)")

# 父元素的倒数第n个子节点
elements = wd.find_elements(By.CSS_SELECTOR,"p:nth-last-child(2)")

# 父元素的第几个某类型的子节点 可以指定选择的元素是父元素的第几个某类型的子节点
# 使用span:nth-of-type(2) == span:nth-child(2)

# 当然也可以反过来， 选择父元素的 倒数第几个某类型 的子节点
# 使用 nth-last-of-type
# 像这样
# p:nth-last-of-type(2)

for element in elements:
    print('-----------')
    print(element.text)