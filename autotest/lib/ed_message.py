from cgitb import handler
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pytest
from lib.login_success import login_succ

def edit_user(username,password):
   # 修改信息
   wd = webdriver.Chrome()
   wd.implicitly_wait(10)
   
   wd.get('http://localhost/mgr/sign.html')
   
   # 登录
   login_succ(wd,username,password)
   
   
   #定位元素 编辑  修改元素 
   # .btn-group:nth-child(1) > .btn-green 定位编辑元素
   edit_button = wd.find_element(By.CSS_SELECTOR,'.content>div:nth-of-type(3) .search-result-item-actionbar label:nth-of-type(1)').click()
   
   # input[value = '南京中医院']
   edit_msg = wd.find_element(By.CSS_SELECTOR,".content>div:nth-of-type(3)>div>div:nth-of-type(1)>input")
   edit_msg.clear()
   edit_msg.send_keys('南京省中医院')
   # .btn-group > .btn-green 确定
   sure_button = wd.find_element(By.CSS_SELECTOR,'.btn-group > .btn-green').click()
   
   # 获取修改后的信息
   actual_result = ''
   
   customer_info = wd.find_elements(By.CSS_SELECTOR,".content div:nth-child(3) .search-result-item-field span:nth-child(2)")     
   for element in customer_info[0:3]:
      actual_result += ''.join(element.text)
      
   print(f'列表中显示的客户信息为：{actual_result}')    
        
   #预期结果
   excepted_result = '南京省中医院166784001南京中医院120号'
   print(f'预期结果为：{excepted_result}')
        
   #判断
   try:
      assert excepted_result == actual_result
      print('UI_0103 PASS')
   except Exception as e:
      print('UI_0103 FAIL ',format(e))
         
   sleep(1)
   wd.quit()
   
# 添加药品
def create_medicens(username,password):
   wd = webdriver.Chrome()
   wd.implicitly_wait(10)
   
   wd.get('http://localhost/mgr/sign.html')
   login_succ(wd,username,password)
   
   # 定位药品元素
   med = wd.find_element(By.XPATH,'//*[@id="root"]/aside/section/ul/li[3]/a/span')
   med.click()
   
   # 添加药品
   cmed = wd.find_element(By.CSS_SELECTOR,'button > span')
   cmed.click()
   
   # .col-lg-8 div input:nth-child(1) 药品名称
   wd.find_element(By.CSS_SELECTOR,".col-lg-8 div:nth-child(1) input  ").send_keys('青霉素盒装')
   
   # 编号
   wd.find_element(By.CSS_SELECTOR,'.col-lg-8 div:nth-child(2) input ').send_keys('YP-32342341')
   
   # 描述
   wd.find_element(By.CSS_SELECTOR,'.col-lg-8 div textarea').send_keys('青霉素注射液，每支15ml，20支装')
   
   # 创建
   wd.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()
   
   actual_result = ''
   
   # .content-wrapper .search-result-item span:nth-child(2)
   
   medicine_info = wd.find_elements(By.CSS_SELECTOR,".content div:nth-child(3) .search-result-item-field span:nth-child(2)")     
   for element in medicine_info[0:3]:
      actual_result += ''.join(element.text)
      
   print(f'列表中显示的药品信息为：{actual_result}')    
        
   #预期结果
   excepted_result = '青霉素盒装1YP-32342341青霉素注射液，每支15ml，20支装'
   print(f'预期结果为：{excepted_result}')
        
   #判断
   try:
      assert excepted_result == actual_result
      print('UI_0105 PASS')
   except Exception as e:
      print('UI_0105 FAIL ',format(e))
         
   sleep(1)
   wd.quit()


   
def click_web(username,password):
   # 点击网页
   wd = webdriver.Chrome()
   wd.implicitly_wait(10)
   
   wd.get('http://localhost/mgr/sign.html')
   login_succ(wd,username,password)
   
   # 最大化窗口
   wd.maximize_window()
   
   # 记录当前页面
   # mainWindow 变量保存当前窗口的句柄
   mainWindow = wd.current_window_handle
   url1 = wd.current_url
   print(f'当前页面地址为:{url1}')
   
   # 定位网页页面
   webui = wd.find_element(By.XPATH,'//*[@id="root"]/footer/div/a')
   webui.click()
   
   sleep(1)
   
   
  
   for handler in wd.window_handles:
      # 先切换到该窗口
      wd.switch_to.window(handler)
      # 获取该网页的标题
      if '白月黑羽' in wd.title:
         break
   
   actual_result = ''
   
   # .content-wrapper .search-result-item span:nth-child(2)
   
   menu_info_list = wd.find_elements(By.CSS_SELECTOR,".navbar-nav .nav-item span")     
   for menu in menu_info_list:
      actual_result += ''.join(menu.text)
      
   print(f'列表中主题信息为：{actual_result}')    
        
   #预期结果
   excepted_result = 'Python基础Python进阶Qt图形界面Django自动化测试性能测试HTML/CSSJS语言JS Web'
   print(f'预期结果为：{excepted_result}')
        
   #判断
   try:
      assert excepted_result == actual_result
      print('UI_0106 PASS')
   except Exception as e:
      print('UI_0106 FAIL ',format(e))
      
   # 通过保存的句柄切换到老窗口
   wd.switch_to.window(mainWindow)
   url2 = wd.current_url
   print(f'返回页面地址为：{url2}')
   
   try:
      assert url1 == url2
      print('UI_0106 PASS,返回页面成功')
   except Exception as e:
      print('UI_0106 FAIL,返回页面失败',format(e))
   
   sleep(1)
   # 点击管理员
   wd.find_element(By.CSS_SELECTOR,'.user .dropdown-toggle').click()
   wd.find_element(By.CSS_SELECTOR,'.user-footer .pull-right').click()
   