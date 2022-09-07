from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# 创建 Webderive对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

# 调用webDriver对象的get方法，可以让浏览器打开指定网址
wd.get('https://www.byhy.net/_files/stock1.html')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element(By.ID,'kw')

# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
element.send_keys("投资")

# 通过点击按钮的元素来执行信息
element = wd.find_element(By.ID,"go")
element.click()


#退出
# wd.quit()