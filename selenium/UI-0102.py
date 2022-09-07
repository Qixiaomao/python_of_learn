from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

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

# 点击客户信息
clik = wd.find_element(By.CSS_SELECTOR,'.content>.col-lg-12>button')
clik.click()

# 输入客户信息
customer_name = wd.find_element(By.CSS_SELECTOR,'.col-lg-8 div:nth-child(1) input')
customer_name.send_keys('南京中医院')

# 联系电话
customer_ph = wd.find_element(By.CSS_SELECTOR,".col-lg-8 div:nth-child(2) input")
customer_ph.send_keys('1567889990')

#地址
#customer_add = wd.find_element(By.CSS_SELECTOR,".col-lg-8 div:nth-child(3) textarea")
#customer_ph.send_keys('南京中医院11111')

# 点击创建
create_button = wd.find_element(By.CSS_SELECTOR,'.content>.col-lg-12>.col-lg-12 button:nth-child(1)')
create_button.click()


# 实际结果
actual_result = ''

customer_info = wd.find_elements(By.CSS_SELECTOR,".content>div:nth-of-type(3) .search-result-item-field>span:nth-child(2)")
for element in customer_info:
    actual_result += ''.join(element.text)
    
print(f'列表中显示的客户信息为：{actual_result}')

# 预期结果
expected_result = '南京中医院1567889990'
print(f'预期结果为:{expected_result}')

#若有异常进行判断
try:
    assert expected_result == actual_result
    print('UI-0102 PASS,结果与预期一致')
except Exception as e:
    print('UI-0102 FAIL,实际与预期结果不一致',format(e))
    

sleep(3)
wd.quit()