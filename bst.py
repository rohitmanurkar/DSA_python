class node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
root =node(5)
A = node(1)
B = node(8)
c = node(-1)
d = node(3)
e = node(7)
f = node(9)

root.left = A
root.right = B
A.left = c
A.right = d
B.left = e
B.right = f


#BST Insertion

def in_order(n):
    if not n:
        return
    if n.left:
     in_order(n.left)
    print(n)
    if n.right:
        in_order(n.right)

in_order(root)
print("----------------------------------------")

#search in BST

def search_bst(n, target):
    if not n:
        return False
    if n.val == target:
        return True
    if target<n.val:
        return search_bst(n.left, target)
    else:
        return search_bst(n.right, target)
    
print(search_bst(root,0))