from hytest import *

class c1:
    tags = ['C1测试']
    name = '登录测试 C1'
    
    def teststeps(self):
        wd = GSTORE['wd']
        wd.get('http://localhost/mgr/sign.html')
        
        # 第1个参数是 webdriver 对象
        # width 参数为可选参数， 指定图片显示宽度
        SELENIUM_LOG_SCREEN(wd, width='70%') 