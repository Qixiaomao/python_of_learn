# select单选框
# 导入selectl类
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

# 创建select对象
select = Select(wd.find_element(By.ID,'ss_single'))

# 通过select 对象选中小雷老师
select.select_by_visible_text("小雷老师")