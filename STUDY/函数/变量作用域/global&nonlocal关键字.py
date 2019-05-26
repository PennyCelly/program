# 修改全局变量 num
# num = 1
#
#
# def print1():
#     global num            # global要放在函数内顶部
#     print(num)
#     num = 123             # global之后，才可以在函数内赋值
#     print(num)
#
#
# print1()
# print(num)


# 修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字
def outer():
    num = 0

    def iner():
        num = 123               # 只修改了iner函数内num的值
        print(num)
    iner()
    print(num)                  # iner函数外依旧是outer函数定义的值


outer()


# 例子：nonlocal
def outer():
    num = 0

    def iner():
        nonlocal num
        num = 123               # 同时也修改了outer函数内num的值
        print(num)
    iner()
    print(num)


outer()
