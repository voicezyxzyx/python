# #栈：先进后出
# stack = []
#
# #压栈（向栈内存数据）
# stack.append('A')
# stack.append('B')
# stack.append('C')
# print(stack)
#
# #出栈（取出栈内数据）
# stack.pop()
# print(stack)
#


#队列  先进先出

import collections
#创建一个队列
queue=collections.deque()
print(queue)
#进队
queue.append('A')
queue.append('b')
queue.append('c')
print(queue)

#出队列
queue.popleft()
print(queue)

