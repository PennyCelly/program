"""
集合
一、特点及创建
1.集合是无序的不重复元素序列
2.创建方法：
  ①param1= {value1，value2，...}
  ②set(value)
  ③空集合-set（）                                        #set{}是创建空字典
"""
# 去重功能
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# 快速判断元素是否在集合内
print('orange' in basket)
"""
二、集合间的运算
1.a-b                                                 a减去b里有的元素
2.a | b                                               a和b里的所有元素（去重）
3.a & b                                               a和b都有的元素
4.a ^ b                                               a和b不同时有的元素

三、集合的基本操作
1.s.add( x )                                          将元素 x 添加到集合 s 中
2.s.update( x )                                       添加元素，且参数可以是列表，元组，字典等
3.s.remove(x)                                         将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误
4.s.discard(x)                                        移除集合中的元素，且如果元素不存在，不会发生错误
5.s.pop(x)                                            随机删除集合中的一个元素
6.len(s)                                              计算集合 s 元素个数
7.s.clear                                             清空集合
8.x in s                                              判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。
9.difference()                                        返回多个集合的差集,即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中，且返回一个新集合
10.difference_update()                                用于移除两个集合中都存在的元素, difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
11.intersection()                                     返回集合的交集,且返回一个新集合
12.set.intersection_update(set1, set2 ... etc)        返回两个集合的交集，在原始集合上更改
13.isdisjoint()                                       判断两个集合是否包含相同的元素，没有返回True，有返回false
14.issubset()                                         判断集合的所有元素是否都包含在指定集合中,如果是则返回 True，否则返回 False。        x.issubset(y)------判断集合 x 的所有元素是否都包含在集合 y 中
15.issuperset(set)                                    判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。  x.issuperset(y) ---判断集合 y 的所有元素是否都包含在集合 x 中
16.pop()                                              随机移除元素
17.remove()                                           移除指定元素,移除一个不存在元素时，会发生错误
18.discard()                                          移除指定元素,移除一个不存在元素时，不会发生错误
19.symmetric_difference()                             返回两个集合中不重复的元素集合,会移除两个集合中都存在的元素,返回新集合
20.symmetric_difference_update()                      返回两个集合中不重复的元素集合,会移除两个集合中都存在的元素，更新原有集合
21.union()                                            返回两个集合的并集
22.update()                                           给集合添加新元素
"""
set1 = set(('a', 'b', 'c', 'd', 'e', 'f'))
print(set1)
# s.add(x)
set1.add('g')                                        # 只能添加一个元素
print(set1)
# s.update(x)
set1.update('t', 'h', 'i', '2e')                     # 可以添加多个元素
print(set1)
set1.update({'1', '2'}, (1, 2), ['adf', 'f23'])      # 可以添加列表、元组、集合的元素
print(set1)
# s.remove(x)                                        # remove移除不存在元素，会报错
set1.remove('a')
print(set1)
# s.discard(x)
set1.discard('a')                                    # discard移除不存在元素，不会报错
print(set1)
# s.pop(x)                                           # 随机删除
x = set1.pop()
print(set1, x)
# len(s)
print(len(set1))
# x in s
print('f23' in set1)
# s.difference
set2 = {'1', '2', 3, 1, 4, 'tired'}
set3 = set1.difference(set2)
print(set3)                                           # 即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中
set1.difference_update(set2)
print(set1)                                           # difference_update方法没有返回值，直接在set1中移除元素
# s.clear
set1.clear()
print(set1)
# s.intersection(x,y,z...)
set_a = {'1', '2', 'a', 'b', 1, 2, 3}
set_b = {'a', 'b', 'c'}
set_c = set_a.intersection(set_b)                     # 返回两个集合的交集，且返回一个新集合
print(set_c)
# intersection_update()
set_a.intersection_update(set_b)                      # 返回两个集合的交集，在原始集合上更改
print(set_a)
# isdisjoint.()                                       # 不包含返回True,包含返回False
x = set_a.isdisjoint(set_b)
print(x)
# issubset()                                          # 判断set_a是否包含在set_b中
print(set_a.issubset(set_b))                          # set_a为{'b', 'a'}，都包含在set_b中，包含返回True，不包含返回False
# issuperset()
print(set_a.issuperset(set_b))                        # 判断set_b是否包含在set_a中
# pop()
x = set_b.pop()
print(set_b, x)
# symmetric_difference()
set_x = {'a', 'b', 'c', 'd', 'e'}
set_y = {'f', 'g', 'h', 'i', 'e'}
set_z = set_x.symmetric_difference(set_y)              # 移除两个集合中重复元素，生成新集合
print(set_z)
# symmetric_difference_update()                        # 移除两个集合中重复元素，在原集合上修改
set_x.symmetric_difference_update(set_y)
print(set_x)
# union()
set_m = set_x.union(set_y)                             # 并集
print(set_m)
# update()
print(set_x)
set_x.update('zx', '999', {1, 2})
print(set_x)
