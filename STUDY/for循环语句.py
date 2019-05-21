"""
----------------------------for 循环语句-------------------------------
1.for循环：遍历任何序列的项目，如一个列表或者一个字符串【遍历数字序列用内置函数range()】
2.一般for格式：
for <variable> in <sequence>:
    <statements>
else:
    <statements>
for 循环正常执行结束后，else 语句里面的内容也会正常执行，如果for break退出了，则不执行else的内容
"""
# !/usr/bin/python3

list1 = ['Baidu', 'Google', 'Taobao', 'Tianmao']
for x in list1:
    print(x)
else:
    print("已遍历完所有元素")


sites = ["Baidu", "Google", "Runoob", "Taobao"]
x = 'Taobao'
for site in sites:
    if site == x:                                 # x如果在列表中，则会break结束for循环，且不会执行else的语句
        print("淘宝")
        break
    print("循环数据"+site)
else:                                            # for循环全部遍历之后，会去执行else的语句
    print("该数据不在列表中")
print("循环完成！")

# 遍历字典的key和value
dict_a = {'购物': '淘宝', '查询': '百度', '买车': '汽车之家', '学习': '知乎', '娱乐': '新浪'}
for keys in dict_a.keys():
    print(keys, dict_a[keys])

"""
-----------------------------------range()函数-----------------------------------
需要遍历数字序列，可以使用内置range()函数，它会生成数列
"""
# 区间值
for i in range(101, 110):
    print(i, end=',')
else:
    print("打印101到110间的整数")

# 步长
for i in range(101, 110, 3):
    print(i, end=',')
else:
    print("在区间101-110，每隔3位取一个数字")

# 步长为负数
for i in range(-101, -110, -3):
    print(i, end=',')
else:
    print("在区间101-110，每隔3位取一个数字")

# 遍历序列索引
list_a = ['a', 'b', 'c', 'd', 'e']
for i in range(len(list_a)):
    print(i, list_a[i])

# range()创建列表
list_b = list(range(5))
print(list_b)


"""
--------------------break和continue语句及循环中的else子句---------------------
1.从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
"""
