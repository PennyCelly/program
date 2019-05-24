"""
默认参数
1.调用函数时，如果没有传递参数，则会使用默认参数。
"""


# 没有传递age，则使用默认参数
def printme(name, age=23):
    print("名字：", name)
    print("年龄：", age)


printme(name="小二")
print("-------------------")
printme(name="小三", age=29)
