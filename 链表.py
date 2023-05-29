class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkList():
    def __init__(self, node = None):
        self.head = node
    def rightInsert(self, x, y):
        # x的右边添加y
        pre = self.head
        while pre.val != x: pre = pre.next
        node = Node(y)
        node.next = pre.next
        pre.next = node

import time
star = time.time()
node = Node(0)
li = SingleLinkList(node)
for i in range(1, 10000000): # 5s
    li.rightInsert(0, i)
"""
li = [0]
for i in range(1, 10000000): # 1h+
    li.insert(0, i)
"""
end = time.time()
print(end - star)
    
    
