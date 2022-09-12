from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pytest

def login_web(username,password):
        
        # 不输入管理员账号输入密码 88888888 登录
        wd = webdriver.Chrome()
        wd.implicitly_wait(10)
        
        wd.get('http://localhost/mgr/sign.html') 
        
        # 输入账号密码
        if username is not None:
           wd.find_element(By.ID,'username').send_keys(username)
        if password is not None:
           wd.find_element(By.ID,'password').send_keys(password)
        wd.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[3]/div/button').click()
        
        sleep(1)
        
       
        
        # 返回alert值
        alertText = wd.switch_to.alert.text
        return alertText
        
        
        
        
        