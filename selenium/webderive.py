from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# 创建 Webderive对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(service=Service(r"D:\tools\chromedriver_win32(1)\chromedriver.exe"))

# 设置了path环境变量之后可以省略掉以上部分
wd = webdriver.Chrome()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

