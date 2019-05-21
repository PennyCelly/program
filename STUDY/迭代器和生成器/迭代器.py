"""
创建一个迭代器
1.把一个类作为一个迭代器使用，需要在类中实现两个方法 __iter__() 与 __next__() 。
2.当类的构造函数为 __init__(), 它会在对象初始化的时候执行。
3.__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
4.__next__() 方法会返回下一个迭代器对象。
"""
# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


classMynumbers = Mynumbers()
myiter = iter(classMynumbers)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))