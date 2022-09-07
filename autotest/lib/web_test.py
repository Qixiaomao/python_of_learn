# 存放公共代码
from selenium import webdriver
from selenium.webdriver.common.by import By
from hytest import *
from time import sleep

def open_browser():
    INFO('打开浏览器')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)

    wd.get('http://127.0.0.1/mgr/sign.html')
    
    GSTORE['wd'] = wd
    
def mgr_login():
    INFO('用管理员账户登录')
    
    wd = GSTORE['wd']
    wd.get('http://127.0.0.1/mgr/sign.html')
    wd.find_element(By.ID,'username').send_keys('byhy')
    wd.find_element(By.ID,'password').send_keys('88888888')

    wd.find_element(By.TAG_NAME,'button').click()    
    