# 相邻兄弟节点的选择
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample1b.html')

'''
上面的例子里面，我们要选择 唐诗 和宋词 的第一个 作者

还有一种思考方法，就是选择 h3 后面紧跟着的兄弟节点 span。

这就是一种 相邻兄弟 关系，可以这样写 h3 + span

表示元素 紧跟关系的 是 加号
'''
# element = wd.find_element(By.CSS_SELECTOR,"#t1 h3+span")

# print('--------')
# print(element.text)

'''
后续所有兄弟节点选择
如果要选择是 选择 h3 后面所有的兄弟节点 span，可以这样写 h3 ~ span

'''
elements = wd.find_elements(By.CSS_SELECTOR,"h3~span")

for element in elements:
    print('---------')
    print(element.text)