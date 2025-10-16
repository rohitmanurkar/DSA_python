from collections import deque


class node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

root =node(1)
A = node(2)
B = node(3)
c = node(4)
d = node(5)
e = node(6)

root.left = A
root.right = B
A.left = c
A.right = d
B.right = e

#BFS traversal of a binary tree

def bfs_tra(root):
    if  not root:
        return
    q = deque()
    q.append(root)

    while q:
        curr = q.popleft()
        print(curr)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

print("BFS Traversal")
bfs_tra(root)
print("----------------------------------------")