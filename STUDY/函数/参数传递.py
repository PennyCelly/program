# !/usr/bin/python3
"""
1.在 python 中，类型属于对象，变量是没有类型的
ex: a =  [1, 2, 3]
    a = "hello"
[1, 2, 3]类型是列表，"hello"类型是string，a仅是一个对象的引用（一个指针），可以指向list，也可以指向string
2.参数修改
  不可更改的对象：strings, tuples, numbers
  可以修改的对象：list,dict
①不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
②变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
3.参数传递
①不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
②可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
"""


# 传不可变对象实例
def ChangeInt(a):
    a = 10
    print(a)


b = 2                                    # b指向int 2
ChangeInt(b)                             # 复制了变量b，且让a和b指向了同一个int对象 10
print(b)
print(ChangeInt(b))


# 传可变对象实例
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值：", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数内取值：",  mylist)
