"""
1.迭代器是访问集合元素的一种方式
2.迭代器是一个可以记住遍历的位置的对象
3.迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
4.两个基本方法：iter() 和 next()
"""
# 字符串，列表或元组对象都可用于创建迭代器：
list1 = [1, 2, 3, 4, 56, 78]
it1 = iter(list1)
print(next(it1))
print(next(it1))
print(next(it1))
# 迭代器对象可以使用常规for语句进行遍历
for i in it1:                               # python next()迭代器完成会引发StopIteration异常
    print(i)
# 也可以使用 next() 函数
import sys
list2 = ['a', 'b', 'c', 'd', 'e', 'd']
it2 = iter(list2)
while True:
    try:
        print(next(it2))
    except StopIteration:                   # for循环自带处理异常，while循环需要处理异常
        sys.exit()