from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

# wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
wd.get('https://cdn2.byhy.net/files/selenium/sample1a.html')

# 选择语法的联合使用 方法一：.footer1 > .date  
# 方法二：.footer1 .date
# 方法三：div.footer1 > span.date
# element = wd.find_element(By.CSS_SELECTOR,".footer1 > .date")

# 组选择：同时选择class为plant 和 class animal的情况，就用.plant, .animal
# elements = wd.find_elements(By.CSS_SELECTOR,".plant, .animal")

# for element in elements:
#     print("-------------")
#     print(element.text)
    
# 另外注意：组选择结果列表中，选中元素排序， 不是 组表达式的次序， 
# 而是符合这些表达式的元素，在HTML文档中的出现的次序。

elements = wd.find_elements(By.CSS_SELECTOR,"#t1 > span, #t1 > p")

for element in elements:
    print("-----------")
    print(element.text)