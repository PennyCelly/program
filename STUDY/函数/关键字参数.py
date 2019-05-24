"""
关键字
1.关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
2.使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
"""


# 在函数 printme() 调用时使用参数名
def printme(str):
    print(str)
    return


printme(str='hello')


# 函数参数的使用不需要使用指定顺序
def area(width, height):
    area = width*height
    print(area)


area(height=12, width=10)
