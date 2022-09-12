# 登录测试

from lib.login import login_web


def setup_module():
    print("\n *** 初始化模块清除 ***")
    
def teardown_module():
    print("\n *** 清除-模块 ***")
    
    

class Test_UI000x:
    
    def test_UI0001(self):
        print('\n 用例 UI0001')
        alertText = login_web(None,'88888888')
        assert alertText=='请输入用户名'
        
    def test_UI0002(self):
        print('\n 用例 UI0002')
        # 正确的管理员账号 byhy  不输入密码
        alertText = login_web('byhy',None)
        assert alertText=='请输入密码'
        
    def test_UI0003(self):
        print('\n 用例 UI0003')
        # 正确的管理员账号 byh  输入密码88888888
        alertText = login_web('byh','88888888')
        assert alertText=='登录失败 : 用户名或者密码错误'
    
    def test_UI0004(self):
        print('\n 用例 UI0004')
        # 正确的管理员账号错误的密码8888888
        alertText = login_web('byhy','8888888')
        assert alertText=='登录失败 : 用户名或者密码错误'  
    
    def test_UI0005(self):
        print('\n 用例 UI0005')
        # 正确的管理员账号错误的密码888888888
        alertText = login_web('byhy','888888888')
        assert alertText=='登录失败 : 用户名或者密码错误'     
    
    
        