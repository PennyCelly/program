"""
不定长参数
需要一个函数能处理比当初声明时更多的参数，这些参数叫做不定长参数
"""
print('不定长参数-元祖'.center(70, '-'))


def nqconfig(a, *b):              # 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
    print(a)
    print(b)


nqconfig(2, 3, 4, 5)
print('不定长参数-空元祖'.center(70, '-'))


# 在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量
def nqconfig2(a, *b):
    print(a)
    print(b)
    for x in b:
        print(x)


nqconfig2(2)
print('不定长参数-字典'.center(70, '-'))


def nqconfig_dic(a, **b):
    print(a)
    print(b)


nqconfig_dic(2, x=3, y=4, z=5)
print('单独*必须要用关键字传入')


def nqconfig3(a, b, *, c):
    print(a+b+c)


nqconfig3(1, 2, c=3)                 # 单独*必须要用关键字传入
