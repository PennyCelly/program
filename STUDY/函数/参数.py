#### 必须参数
"""
1.必须参数须以正确的顺序传入函数。
2.调用时的数量必须和声明时一样
3.调用printme（）函数时，必须传入一个参数，不然会出现语法错误
"""
# printme()必须传入参数
def printme(str):
    print(str)
    return


# 调用printme函数
printme()


#### 关键字参数
"""
1.关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
2.使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
"""