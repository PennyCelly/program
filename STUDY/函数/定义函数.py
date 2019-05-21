#!/usr/bin/python3
"""
定义函数规则：
1.以def关键词开头，后接函数标志符号名称和圆括号（）
2.圆括号之间可以用于定义参数，任何传入参数和自变量必须放在圆括号中间
3.函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明
4.函数内容以冒号起始，并且缩进
5.return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""


# 计算面积函数
def area(width, height):
    return width*height


def print_welcome(name):
    print("welcome", name)


# 函数调用
print_welcome("小二")
w = 5
h = 19
print("width=", w, "height=", h, "area=", area(w, h))
