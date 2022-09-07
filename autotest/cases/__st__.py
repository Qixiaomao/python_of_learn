from hytest import *
from lib.web_test import *

# 初始化用例
def suite_setup():
    INFO('suite_setup')
    open_browser()
    
        
# 清除
def suite_teardown():
    INFO('suite_teardown')
    wd = GSTORE['wd']
    wd.quit()