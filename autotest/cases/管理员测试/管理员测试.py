from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from hytest import *





# 建议：类名 对应 用例编号
class UI_0101:
    # 测试用例名字，也建议以用例编号结尾，方便 和 用例文档对应
    # 也方便后面 根据用例名称 挑选执行
    name = '检查左侧菜单 - UI-0101'

    # 测试用例步骤
    def teststeps(self):
        STEP(1,'获取左侧菜单信息')
        wd = GSTORE['wd']
        elements = wd.find_elements(By.CSS_SELECTOR,'.sidebar-menu li span')
        
        menuText = [element.text for element in elements]
        
        STEP(2,'检查菜单栏左侧信息')
        CHECK_POINT('左侧菜单检查',menuText[:3] == ['客户','药品','订单'])
        
class UI_0102:
    name = '添加客户 UI_0102'
    def teststeps(self):
        STEP(1, '点击左侧客户菜单')
        wd = GSTORE['wd']

        # 先找到上层节点，缩小查找范围
        sidebarMenu = wd.find_element(By.CLASS_NAME,'sidebar-menu')

        # 再找到内部元素
        elements = sidebarMenu.find_elements(By.TAG_NAME,'span')

        # 第一个span对应的菜单是 客户，点击它
        elements[0].click()


        STEP(2, '添加客户')

        # 点击添加客户按钮
        wd.find_element(By.CLASS_NAME,'glyphicon-plus').click()

        # form-contorl 对应3个输入框
        inputs = wd.find_elements(By.CSS_SELECTOR,'.add-one-area .form-control')

        # 输入客户姓名
        inputs[0].send_keys('南京中医院')
        # 输入联系电话
        inputs[1].send_keys('2551867858')
        # 输入客户描述
        inputs[2].send_keys('江苏省-南京市-秦淮区-汉中路-16栋504')

        # 第1个 btn-xs 就是创建按钮， 点击创建按钮
        wd.find_element(By.CSS_SELECTOR,'.add-one-area .btn-xs').click()

        # 等待1秒
        sleep(1)


        STEP(3, '检查添加信息')

        # 找到 列表最上面的一栏
        item = wd.find_elements(By.CLASS_NAME,'search-result-item')[0]

        fields = item.find_elements(By.TAG_NAME,'span')[:6]

        texts = [field.text for field in fields]
        INFO(texts)

        # 预期内容为
        expected = [
            '客户名：',
            '南京中医院',
            '联系电话：',
            '2551867858',
            '地址：',
            '江苏省-南京市-秦淮区-汉中路-16栋504'
        ]

        CHECK_POINT('客户信息和添加内容一致 ',
                    texts == expected)
                    
     
        
        