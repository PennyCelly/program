from STUDY.基础定义.ChangeColor import bcolors
"""
Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
"""
'''
Python支持四种不同的数字类型
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）[python3自动会将int扩展]
float（浮点型）
complex（复数）
'''


'''
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
内置的 type() 函数可以用来查询变量所指的对象类型。
'''
###变量赋值
print(bcolors.RED+'====================变量赋值========================')
a, b, c = 1, 2, 'runboo'
print(a, b, c)
print(bcolors.RED+'====================变量赋值========================\n')



print(bcolors.GREEN+'------------------Number ----------------------')
a = 2
a_type_str="a的type:"
print(bcolors.RED+a_type_str + repr(type(a)))   #repr()将object转化为字符串类型
a_id_str = "a的id"
a_id = id(a)
print(a_id_str + repr(id(a)))
print("a改变数值之后")
a = 3
print(a_type_str + repr(type(a)))   #repr()将object转化为字符串类型
print(a_id_str + repr(id(a)))
print(bcolors.GREEN+'------------------Number ----------------------')
print('\n')




'''
python的字串列表有2种取值顺序:
从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
可以使用 [头下标:尾下标] 来截取相应的字符串，
1.其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
2.获取的子字符串 包含 头下标 的字符，但  不包含  尾下标  的字符。
3.加号（+）是字符串连接运算符，星号（*）是重复操作
'''

print(bcolors.YELLOW+'------------------string ----------------------')
name = '杜玮'
name1 = 'crystal.du'
age = '24'

var1 = 1
var2 = 2
name1 = name1[0:7]
print("获取的子字符串不包含 尾下标字符:"+name1)
str = "Hello World!"
str_type_str = "name的类型为："
print(str_type_str + repr(type(name)))
print(str)            # 输出完整字符串
print(str[0])         # 输出字符串中的第一个字符
print(str[2:5])       # 输出字符串中第三个至第五个之间的字符串
print(str[2:])        # 输出从第三个字符开始的字符串
print(str[0:5]*2)     # 输出字符串两次
print(str+"TEST")  # 输出连接的字符串


'''
Python 列表截取可以接收第三个参数，
参数作用是截取的步长，
以下实例在索引 1 到索引 4 的位置,
设置为步长为 2（间隔一个位置）来截取字
'''
letters = "123456789"
print(letters[0:9:2])       #0代表第1位，9代表最后1位,2代表步长为2来截取数字

print(bcolors.YELLOW+'------------------string ----------------------')
print('\n')


print(bcolors.BLUE+'------------------list ----------------------')
'''
List（列表）
列表用 [ ] 标识，是 python 最通用的复合数据类型。
列表可以完成大多数集合类的数据结构实现。
它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
'''

list1 = ["test", "shelry", "123", "+++", "1994.02.26", "35.12"]
list1_1 = list1[0:] * 2
list1_2 = list1[1] + "-" + list1[4]
list1[1] = "DuWei"
print(list1)
print(list1_1)
print(list1_2)
print(list1[0:9:2])   ##0代表第1位，9代表最后1位,2代表步长为2来截取数字
print(bcolors.BLUE+'--------------------list--------------------')
print('\n')





'''
Tuole 元组是另一个数据类型，类似于 List（列表）。
元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
'''

print(bcolors.BLACK+'--------------------tuple--------------------')
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
onetuple = (1,)

print(tuple)                 # 输出完整元组
print(tuple[0])              # 输出元组的第一个元素
print(tuple[1:3])            # 输出第二个至第三个的元素
print(tuple[2:])             # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)        # 输出元组两次
print(tuple + tinytuple)    # 打印组合的元组

print('--------------------tuple--------------------')
print('\n')

print(bcolors.GREEN+'-------不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。------------- ')
'''
可变数据类型：value值改变，id值不变；不可变数据类型：value值改变，id值也随之改变。函数 id()
'''

list_test = ['123', 758, 'bcd', 'qaz', '9ol.']
list_test[1] = "列表"

tup = ('你好', 'python', '数组', 333)
tup = (20,)   # 一个元素需要在后面加,
# tup[2] = "这是"
# print(tup[2])
num_test = 2
str_test = "Hello,World!"
num_test = 1.0
str_test = "我变啦！"
print(num_test)
print(str_test)
print('-------不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。------------- ')
print('--------------------tuple--------------------\n\n')


print(bcolors.YELLOW+'--------------------集合--------------------')
kongset = set()                                                        # 而不是kongset={},这种写法是创建一个空字典
student1 = set('abcdefghijklmn')                                       # set()注意是用（）小括号，创建一个名为student1的集合
student2 = {'member1', 'member2', 'member3', 'member4', 'member4'}     # 直接创建student2的集合，注意使用{}中括号
# 集合的运算
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

if 'member1' in student2:
    print('yes')
print(student2)
print('--------------------集合--------------------\n\n')

print(bcolors.GREEN+"---------------------remaining problems---------------------------------------\n"
      + "1.在ChangeColor文件中编写了 模块bcolor ，不会调用改变颜色的函数去对选定的字符串作颜色改变 \n"
      + "---------------------remaining problems---------------------------------------")


print(bcolors.BLUE+'--------------------字典--------------------')
"""
1.字典与列表的区别：①列表-有序的对象结合 ；字典-无序的对象集合    ②列表-元素通过偏移存取 ； 字典-元素通过键来存取
2.字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
   键(key)必须使用不可变类型且唯一。
"""
test_dict = {'y': '研发中心', 'p': '普惠金融', 2: 'have no idea'}
test_dict1 = {'value1': '我是一个字典的value'}
print(test_dict, '\n', test_dict1['value1'], '\n', test_dict[2])
print(test_dict.keys())
print(test_dict.values())

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
dict1 = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
print(dict1.keys())
print('--------------------字典--------------------')


print(bcolors.YELLOW+'--------------------数据类型转换--------------------')
'''
int(x[,base])            将x转换为一个整数
float(x)                将x转换到一个浮点数
complex(real [,imag])   创建一个复数
str(x)                  将对象 x 转换为字符串
repr(x)                 将对象 x 转换为表达式字符串
eval(str)               用来计算在字符串中的有效Python表达式,并返回一个对象tuple(s)将序列 s 转换为一个元组
list(s)                 将序列 s 转换为一个列表
set(s)                  转换为可变集合
dict(d)                 创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)            转换为不可变集合
chr(x)                  将一个整数转换为一个字符
ord(x)                  将一个字符转换为它的整数值
hex(x)                  将一个整数转换为一个十六进制字符串
oct(x)                  将一个整数转换为一个八进制字符串
'''


print('--------------------数据类型转换--------------------')
