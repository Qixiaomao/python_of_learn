from hytest import *
from lib.web_test import *

force_tags = ['登录功能','冒烟测试','UI测试']

# 初始化用例
def suite_setup():
    mgr_login()
        
