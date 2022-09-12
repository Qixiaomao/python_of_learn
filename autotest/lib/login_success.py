from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pytest

def login_succ(wd,username,password): 
        
    # 输入账号密码
    if username is not None:
           wd.find_element(By.ID,'username').send_keys(username)
    if password is not None:
           wd.find_element(By.ID,'password').send_keys(password)
    wd.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[3]/div/button').click()