from distutils.log import info
from hytest import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class UI_000X:
    # ddt_cases 里面每个字典元素 定义一个用例的数据
    # 其中： name是该用例的名称， para是用例的参数
    ddt_cases = [
        {
            'name':'登录 UI-001',
            'para':[None,'88888888','请输入用户名']
        },
        {
            'name':'登录 UI-002',
            'para':['byhy',None,'请输入密码']
        },
        {
            'name':'登录 UI-003',
            'para':['byh','88888888','登录失败 : 用户名或者密码错误']
        }
    ]
    # 调用时，
    # hytest 框架执行时，会自动创建出3份用例实例
    # 并且在调用 teststeps时，把每个用例的参数设置在 self.para 中
    # 用例代码 可以直接从 self.para 中获取参数
    def teststeps(self):
        wd = GSTORE['wd']
        
        wd.get('http://localhost/mgr/sign.html')
        # 取出参数
        username,password,msg = self.para
        
        if username is not None:
            wd.find_element(By.ID,'username').send_keys(username)
        
        if password is not None:
            wd.find_element(By.ID,'password').send_keys(password)
            
        # if (username and password) is not None:
        #     wd.find_element(By.ID,'username').send_keys(username)
        #     wd.find_element(By.ID,'password').send_keys(password)
        
        wd.find_element(By.TAG_NAME,'button').click() 
            
        sleep(2)
        
        notify = wd.switch_to.alert.text
        
        CHECK_POINT('弹出提示',notify == msg)
        
        wd.switch_to.alert.accept()
        
    def teardown(self):
        wd = GSTORE['wd']
        wd.find_element(By.ID,'username').clear()
        wd.find_element(By.ID,'password').clear()
        