"""
一、定义及特点
1.字典是可变容器模型，可存储任意类型对象。
2.字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
"""
# 创建字典
dic1 = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val3'}

"""
二、访问字典里的值
把相应的键放入到方括号中
"""
print(dic1['key1'], dic1['key4'])

"""
三、修改字典
"""
dic1['key4'] = 32
print(dic1)

"""
四、删除字典元素
"""
del dic1['key3']                                              # 删除字典元素
print(dic1)
dic1.clear()                                                  # 清空字典
print(dic1)
del dic1                                                      # 删除字典
# print(dic1)

"""
五、字典键的特性
1.不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2.键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
"""

"""
六、字典内置函数&方法
函数：
1.len(dict)                                                     计算字典元素个数，即键的总数
2.str(dict)                                                     输出字典，以可打印的字符串表示。
3.type(variable)                                                返回输入的变量类型，如果变量是字典就返回字典类型。
方法：
1.radiansdict.clear()                                           清空字典
2.radiansdict.copy()                                            返回一个字典的浅复制
  直接赋值和 copy 的区别
  dict1 =  {'user':'runoob','num':[1,2,3]} 
  dict2 = dict1                                                  # 浅拷贝: 引用对象
  dict3 = dict1.copy()                                           # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
"""
# 深浅拷贝
dict2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5 : [1, 2, 3, 4]}
dict2_1 = dict2                                                 # 浅拷贝，dict2_1会随dict2更改而更改
dict2[1] = 'z'
print(dict2, dict2_1)
dict2_2 = dict2.copy()                                          # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
dict2[4] = 'y'
dict2_2[5].remove(1)
print(dict2, dict2_2)
