#!/usr/bin/python3
"""
一、列表的特点
1.序列内置
2.可进行的操作：索引，切片，加，乘，检查成员
3.列表的数据项不需要具有相同的类型
二、创建列表
只要把逗号分隔的不同的数据项使用方括号括起来即可
"""
# 创建列表
list1 = [123, 'jkjk', 344, '9j992']
# 访问列表中的值
print(list1[0])
print(list1[1:3])                                          # 左闭右开
# 更新列表
list1[0] = '000'
print(list1)
# 删除列表元素
del list1[3]
print(list1)
"""
一、Python列表脚本符操作
1.len（[1,2,3]）                                               	长度
2.[1,2,3]+[3,3,5]                                               组合
3.['a']*4                                                       重复
4.3 in [1,2,3]                                                  元素是否存在于列表中
5.for x in [1,2,3]:print(x,end='')                              迭代
二、Python列表截取与拼接
L=['Google', 'Runoob', 'Taobao']
1.L[2]                                                          读取第三个元素
2.L[-2]                                                         读取从右数第二个元素
3.L[1:]                                                         输出从第二个元素开始后输出所有元素
4.L += L                                                        拼接
三、嵌套列表
a = [1,2,4]
b =[a, b, c]
x = [a, b]
"""
#嵌套列表
a = [1, 2, 4]
b =['a', 'b', 'c']
x = [a, b]
print(x)
"""
四、Python列表函数&方法
函数：
1.len(lsit)                                                      列表元素个数
2.max(lsit)                                                      返回列表元素最大值
3.min(list)                                                      返回列表元素最小值
4.list(seq)                                                      将元组转换为列表
"""
print(len(a))
print(max(b))
print(min(a))
table_n = ('a', 'b', '33f', 'etad')
list_table_n = list(table_n)
print(list_table_n)
"""
方法：
1.list.append(obj)                                               在列表末尾添加新的对象   
2.list.count(obj)                                                统计某个元素在列表中出现的次数
3.list.extend(seq)                                               在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4.list.index(obj)                                                从列表中找出某个值第一个匹配项的索引位置
5.list.insert(index, obj)                                        用于将指定对象插入列表的指定位置
6.list.pop([index=-1])                                           移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7.list.remove(obj)                                               移除列表中某个值的第一个匹配项
8.list.reverse()                                                 反向列表中元素
9.list.sort( key=None, reverse=False)                            key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
                                                                 reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
"""
# 添加新对象
list_table_n.append('hahaha')
print(list_table_n)
# 统计某元素出现次数
print(list_table_n.count('a'))
# 在列表末尾追加另一个序列
list1 = [1, 2, 4, 5]
list2 = ['a', 'b', 'e', 'gfd']
list1.extend(list2)
print(list1)
# list.index(obj)
print(list1.index('gfd'))
# list.insert(index, obj)
list1.insert(3, 'insert')
print(list1)
# list.pop([index=-1])
list_pop = list1.pop(3)
print(list1, list_pop)
# list.remove(obj)
list1.remove('gfd')
print(list1)
# list.reverse()
list1.reverse()
print(list1)
# list.sort(key=None, reverse=False)   True 降序，False 升序（默认）。
list_sort = [1, 2, 3, 99, 502, 5]
list_sort.sort(reverse=True)
print(list_sort)
list_sort.sort(reverse=False)
print(list_sort)

# 获取列表的第二个元素
def takesecond(elem):
    return elem[1]


list_key = [(2, 3), (2, 1), (9, 3), (23, 3, 123), (3, 12, 3, 14)]
key = takesecond
# 指定按照第二个元素排序
list_key.sort(key=takesecond)
print(list_key)
