'''1.自动登录管理员账号
   2.检查左侧菜单'''
   

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('http://127.0.0.1/mgr/sign.html')
# 隐式等待10秒
wd.implicitly_wait(10)

# 登录用户名
username = wd.find_element(By.ID,'username')
username.send_keys('byhy')

# 输入密码
password = wd.find_element(By.ID,'password')
password.send_keys('88888888')

# 点击登录
clik = wd.find_element(By.CLASS_NAME,'col-xs-12')
clik.click()


# 实际情况
actual_result = ''

# 点击菜单：客户，药品，订单
tags = wd.find_elements(By.CSS_SELECTOR,'.sidebar-menu span')
for tag in tags[0:3]:
    actual_result += ''.join(tag.text)
    
print(f'页面前三项菜单名称分别为：{actual_result}')

# 预期结果
expected_result = '客户药品订单'
print(f'预期结果为：{expected_result}')



pass