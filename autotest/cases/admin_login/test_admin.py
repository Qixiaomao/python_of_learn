# 管理员操作
from pydoc import cli
import pytest

from lib.get_element import get_element , created_user
from lib.ed_message import edit_user, create_medicens, click_web
import lib.create_me_user_bat 
from lib.login_success import login_succ


def setup_module():
    print('\n *** 初始化-模块 ***')


def teardown_module():
    print('\n ***   清除-模块 ***')

class Test_UI_010x:
    
    
    # 管理员操作
    def test_UI_0101(self):
        print('成功登录 UI-0101')
        get_element('byhy','88888888')
        
    def test_UI_0102(self):
        print('创建用户 UI-0102')
        created_user('byhy','88888888')
        
    def test_UI_0103(self):
        print('修改用户信息 UI-0103')
        edit_user('byhy','88888888')
        
    def test_UI_0105(self):
        print('添加药品 UI-0105')
        create_medicens('byhy','88888888')
        
    def test_UI_0106(self):
        print('进入新页面 UI-0106')
        click_web('byhy','88888888')
        
    
    def test_UI_0107(self):
        print('添加药品和客户 UI-0107')
        lib.create_me_user_bat.create_med()
        lib.create_me_user_bat.create_customer()
        lib.create_me_user_bat.create_order()
        lib.create_me_user_bat.check_order()
        
      
    
    def test_UI_0108(self):
        print('添加药品和订单 UI-0108')
        lib.create_me_user_bat.del_exist_info()
        lib.create_me_user_bat.create_med()
        lib.create_me_user_bat.create_customer()
        lib.create_me_user_bat.create_order()
        lib.create_me_user_bat.check_order()
        
    
        
    
        
    
        