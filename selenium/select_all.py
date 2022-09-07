# select多选框选项
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

# 创建select对象
select = Select(wd.find_element(By.ID,"ss_multi"))

# 清除所有 已经选中的选项
select.deselect_all()

# 选择小雷老师和小凯老师
select.deselect_by_visible_text("小雷老师")
# select.deselect_by_visible_text("小凯老师")