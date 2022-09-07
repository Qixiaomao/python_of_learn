# 手机模式
from selenium import webdriver
from selenium.webdriver.common.by import By

mobile_phone = {"deviceName":"Nexus 5"}

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation",mobile_emulation)

driver = webdriver.Chrome(desired_capabilities= chrome_options.to_capabilities())

driver.get("http://www.baidu.com")

input()
driver.quit()