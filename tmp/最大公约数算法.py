# 定义一个函数
from re import X
from tkinter import Y


def hcf(x,y):
    """该函数返回两个数的最大公约数"""
    
    # 获取最小值
    if x>y:
        smaller = Y
    else:
        smaller = X
        
    for i in range(1,smaller + 1):
        if((x % i == 0) and (y % i ==0)):
            hcf = i
            
    return hcf

# 用户输入两个数字：
num1 = int(input("please input a one: "))
num2 = int(input("please input two : "))

print(num1,"and",num2,"max: ",hcf(num1,num2))