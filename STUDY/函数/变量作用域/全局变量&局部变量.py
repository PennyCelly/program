"""
1.定义在函数内部的变量拥有一个局部作用域
2.定义在函数外的拥有全局作用域。
3.局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
"""

total = 0
def sum(a, b):
    total = a + b
    print(total)        # 局部变量total
    return total


sum(10, 20)
print(total)             # 全局变量total