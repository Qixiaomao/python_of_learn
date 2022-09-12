from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from lib.login_success import login_succ

def get_element(username,password):
        # 不输入管理员账号输入密码 88888888 登录
        username = username
        password = password
        wd = webdriver.Chrome()
        
        login_succ(wd,username,password)
        # 获取左侧菜单栏
        elements = wd.find_elements(By.CSS_SELECTOR,".sidebar-menu  li  span")
        
        # 实际情况
        actual_result = ''
        
        for element in elements[0:3]:
            actual_result += ''.join(element.text)
        
        print(f'前三项菜单名称为：{actual_result}')    
        
        #预期结果
        excepted_result = '客户药品订单'
        print(f'预期结果为：{excepted_result}')
        
        #判断
        try:
           assert excepted_result == actual_result
           print('UI_0101 PASS')
        except Exception as e:
           print('UI_0101 FAIL ',format(e))
         
        sleep(1)
        wd.quit()
        
def created_user(username,password):
   # 登录账户
   wd = webdriver.Chrome()
   wd.implicitly_wait(10)
        
   wd.get('http://localhost/mgr/sign.html') 
        
   # 输入账号密码
   if username is not None:
           wd.find_element(By.ID,'username').send_keys(username)
   if password is not None:
           wd.find_element(By.ID,'password').send_keys(password)
   wd.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[3]/div/button').click()
   
   # 添加客户
   customer_button = wd.find_element(By.CSS_SELECTOR,".content .col-lg-12 button").click()
   
   # 输入信息 客户名，电话，地址
   customer_name = wd.find_element(By.CSS_SELECTOR,".col-lg-8 > div:nth-child(1) input").send_keys('南京中医院')
   
   customer_phone = wd.find_element(By.CSS_SELECTOR,".col-lg-8 > div:nth-child(2) input").send_keys('166784001')
   
   customer_address = wd.find_element(By.CSS_SELECTOR,".col-lg-8 > div:nth-child(3) textarea").send_keys('南京中医院120号')
   
   # 点击创建
   create_button = wd.find_element(By.CSS_SELECTOR,".col-lg-12 > .col-lg-12 > button:nth-child(1)").click()
   
   # 点击取消按钮
   sleep(1)
   create_button = wd.find_element(By.CSS_SELECTOR,".col-lg-12 > .col-lg-12 > button:nth-child(2)").click()
  
        
   # 实际情况
   actual_result = ''
     
   customer_info = wd.find_elements(By.CSS_SELECTOR,".content div:nth-child(3) .search-result-item-field span:nth-child(2)")     
   for element in customer_info[0:3]:
      actual_result += ''.join(element.text)
        
   print(f'列表中显示的客户信息为：{actual_result}')    
        
   #预期结果
   excepted_result = '南京中医院166784001南京中医院120号'
   print(f'预期结果为：{excepted_result}')
        
   #判断
   try:
      assert excepted_result == actual_result
      print('UI_0102 PASS')
   except Exception as e:
      print('UI_0102 FAIL ',format(e))
         
   sleep(1)
   wd.quit()
   

   
