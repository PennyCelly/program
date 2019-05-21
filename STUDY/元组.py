"""
一、元组特点
1.与列表类似
2.元素不可更改
3.元组中只包含一个元素时，要在元素后面添加逗号
"""
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"                                    # 不需要括号也可以
print(tup1, tup2, tup3)


"""
二、元组的操作
"""
# 元组中只有一个元素
tup4 = (2)
tup5 = (2,)
print(type(tup4), type(tup5))

# 访问元组
print(tup1[2])                                               # 元组可以使用下标索引来访问元组中的值
print(tup2[-1])
print(tup3[1:])

# 修改元祖                                                    元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup6 = tup1 + tup2
print(tup6)

# 删除数组                                                    元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
# del tup6
# print(tup6)

"""
三、元组运算符
1.len((1, 2, 3))                                              计算元素个数
2.(1, 2, 3) + (4, 5, 6)                                       连接
3.('Hi!',) * 4                                                复制
4.3 in (1, 2, 3)                                              元素是否存在                   
5.for x in (1, 2, 3): print (x,)                              迭代
"""
"""
四、元祖索引&截取
1.L[2]                                                          读取第三个元素
2.L[-2]                                                         读取从右数第二个元素
3.L[1:]                                                         输出从第二个元素开始后输出所有元素
4.L += L                                                        拼接
"""
"""
五、元组内置函数
1.len(tuple)                                                    计算元组元素个数
2.max(tuple)                                                    返回元组中元素最大值
3.min(tuple)                                                    返回元组中元素最小值
4.tuple(seq)                                                    将列表转换为元组
"""