"""
堆栈：后进先出
列表用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来
"""
stack = ['q', 'w', 3, 4, 7, 5, 9]
stack.append(8)
for i in stack:
    stack.pop()                         # 到7的时候，7已经被pop掉了，循环截止
    print(stack)
    print(i)

