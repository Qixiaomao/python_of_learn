from selenium import webdriver
from selenium.webdriver.common.by import By

def login():
    wd = webdriver.Chrome()
    # 隐式等待最大10秒

    wd.get('http://127.0.0.1/mgr/sign.html')
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