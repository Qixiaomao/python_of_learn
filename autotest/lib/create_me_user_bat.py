'''
本段代码的测试为 测试文档里对于管理员测试用例
测试用例为 UI-0107 UI-0108
因为7与8的区别就是有无前置条件，只需要调用del_exist_info方法就可以删除之前的消息完成
UI-0108所以一并放在一起
'''
from lib.login_success import login_succ
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

# 数据驱动
# 批量添加数据


wd = webdriver.Chrome()
# 隐式等待10秒
wd.implicitly_wait(10)
# 打开测试网页
wd.get('http://localhost/mgr/sign.html')
# 成功登录
login_succ(wd,'byhy','88888888')


def del_exist_info():
    def del_info():
        elements = wd.find_elements(By.CSS_SELECTOR,'.search-result-item-actionbar label:nth-last-of-type(1)')
        if elements:
          for element in elements:
               element.click()
               wd.switch_to.alert.accept()
               sleep(0.5)
               
    # 先删除订单，因为订单关联药品和客户，存在订单信息
    # 点击菜单栏订单，进入订单信息页面
    order_menu = wd.find_element(By.CSS_SELECTOR,'[href=="#/orders"]')
    order_menu.click()
    del_info()
    
    # 点击菜单栏药品，进入药品信息页面
    medicines_menu = wd.find_element(By.CSS_SELECTOR('[href="#/medicines"]'))
    medicines_menu.click()
    del_info()
    
    # 点击菜单栏客户，进入客户信息页面
    customer_menu = wd.find_element(By.CSS_SELECTOR,'[href="#/customers"]')
    customer_menu.click()
    del_info()
    
def create_med():
    # 创建药品
    # 点击菜单栏药品，进入药品信息页面
    med_menu = wd.find_element(By.CSS_SELECTOR,'[href="#/medicines"]')
    med_menu.click()
    
    # 找到添加药品按钮并点击
    med_button = wd.find_element(By.CSS_SELECTOR,'.content>.col-lg-12>button')
    med_button.click()
    
    # 依次添加3种药品
    medicines_data = [
            ('青霉素盒装1','YP-32342341','青霉素注射液，每支15ml，20支装'),
            ('青霉素盒装2','YP-32342342','青霉素注射液，每支15ml，30支装'),
            ('青霉素盒装3','YP-32342343','青霉素注射液，每支15ml，40支装')          
                      ]
    
    for i in range(len(medicines_data)):
        medicines_name = wd.find_element(By.CSS_SELECTOR,'')
        medicines_name.send_keys(medicines_data[i][0])
        
        medicines_number = wd.find_element(By.CSS_SELECTOR,'')
        medicines_number.send_keys(medicines_data[i][1])
        
        medicines_msg = wd.find_element(By.CSS_SELECTOR,'')
        medicines_msg.send_keys(medicines_data[i][2])
        
        # 创建
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()
        
        sleep(1)
        
    # 点击取消按钮
    sleep(1)
    create_button = wd.find_element(By.CSS_SELECTOR,'。content>.col-lg-12.col-lg-12 button:nth-child(2)')
    create_button.click()
    
    print('药品添加成功')
    
    
def create_customer():
    # 创建客户
   
    customer_menu = wd.find_element(By.CSS_SELECTOR,'[href="#/customer"]')
    customer_menu.click()
    
    # 找到添加药品按钮并点击
    cus_button = wd.find_element(By.CSS_SELECTOR,'.content>.col-lg-12>button')
    cus_button.click()
    
    # 依次添加3种药品
    customer_data = [
            ['南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501'],
            ['南京中医院2','2551867852','江苏省-南京市-秦淮区-汉中路-502'],
            ['南京中医院3','2551867853','江苏省-南京市-秦淮区-汉中路-503']        
                      ]
    
    for i in range(len(customer_data)):
        medicines_name = wd.find_element(By.CSS_SELECTOR,'')
        medicines_name.send_keys(customer_data[i][0])
        
        medicines_number = wd.find_element(By.CSS_SELECTOR,'')
        medicines_number.send_keys(customer_data[i][1])
        
        medicines_msg = wd.find_element(By.CSS_SELECTOR,'')
        medicines_msg.send_keys(customer_data[i][2])
        
        # 创建
        wd.find_element(By.XPATH,'.content>.col-lg-12>.col-lg-12 button:nth-child(1)').click()
        
        sleep(1)
        
    # 点击取消按钮
    sleep(1)
    create_button = wd.find_element(By.CSS_SELECTOR,'.content>.col-lg-12.col-lg-12 button:nth-child(2)')
    create_button.click()
    
    print('客户添加成功')
    
def create_order():
    # 创建订单
   
    order_menu = wd.find_element(By.CSS_SELECTOR,'[href="#/order"]')
    order_menu.click()
    
    # 添加订单信息
    cus_button = wd.find_element(By.CSS_SELECTOR,'.content>.col-lg-12>button')
    cus_button.click()
    
    # 添加订单信息
    order_info = {'order_name':'南京中医院2','customer_name':'南京中医院2','medicens_name':'青霉素盒装1','numbers':'100盒'}
    
    
    # 输入订单信息
    order_name = wd.find_element(By.CSS_SELECTOR,'.col-lg-8 div:nth-child(1) input')
    order_name.send_keys(order_info['order_name'])
            
    # 创建select对象，通过select对象选中 南京中医院2
    customer = Select(wd.find_element(By.CSS_SELECTOR,'.col-lg-8 div:nth-child(2) select'))
    customer.select_by_visible_text(order_info['customer_name'])
    
    # 创建select对象 通过select对象选中 青霉素盒1
    medicines = Select(wd.find_element(By.CSS_SELECTOR,'.col-lg-8 div:nth-child(3) select'))
    medicines.select_by_visible_text(order_info['medicens_name'])
    
    # 选中药品后， 输入药品数量
    sleep(1)
    meds_number = wd.find_element(By.CSS_SELECTOR,'.col-lg-8 div:nth-child(3) div input')
    meds_number.send_keys(order_info['numbers'])
    
    # 点击创建按钮
    create_button = wd.find_element(By.CSS_SELECTOR,'.content>.col-lg-12>.col-lg-12 button:nth-child(1)')
    create_button.click()
    
    # 点击取消按钮
    sleep(1)
    create_button = wd.find_element(By.CSS_SELECTOR,'.content>.col-lg-12>.col-lg-12 button:nth-child(2)')
    create_button.click()
    
    print('订单添加成功')
    
def check_order():
    # 取出列表种新增的订单信息
    order_name = wd.find_element(By.CSS_SELECTOR,'.content>div:nth-of-type(3)>div:nth-of-type(1)>span:nth-child(2)')
    # 实际结果
    auctual_result = order_name.text
    print('列表中显示的订单名称为：',auctual_result)
    
    # 预期结果
    expected_result = '南京中医院2'
    print(f'预期结果为:{expected_result}')
    
    # 判断
    try:
        assert expected_result == auctual_result
        print('UI_0107 PASS')
    except Exception as e:
        print('UI_0107 FAIL')
        

