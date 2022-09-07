# 切换到新窗口
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')

# 点击打开新窗口的链接
link = wd.find_element(By.TAG_NAME, "a").click()


# 如下代码切换到对应网页窗口的ID
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是否是要找的窗口
    if 'Bing' in wd.title:
        # 如果是，就跳出循环
        break

'''
因为我们一开始就在 原来的窗口里面，我们知道 进入新窗口操作完后，还要回来，可以事先 
保存该老窗口的 句柄，使用如下方法

# mainWindow变量保存当前窗口的句柄
mainWindow = wd.current_window_handle
切换到新窗口操作完后，就可以直接像下面这样，将driver对应的对象返回到原来的窗口

#通过前面保存的老窗口的句柄，自己切换到老窗口
wd.switch_to.window(mainWindow)

'''

# wd.title属性是当前窗口的标题栏 文本
print(wd.title)