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

# RECURSION APPROACH 
#Pre-order DFS node->left->right

def pre_order_dfs(node):
    if not node:
        return
    print(node)
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

print("Pre-order DFS")
pre_order_dfs(root)
print("----------------------------------------")
#in-order DFS left->node->right
def in_order_dfs(node):
    if not node:
        return
    in_order_dfs(node.left)
    print(node)
    in_order_dfs(node.right)

print("In-order DFS")
in_order_dfs(root)

print("----------------------------------------")
#post-order DFS left->right->node
def post_ord_dfs(node):
    if not node:
        return
    post_ord_dfs(node.left)
    post_ord_dfs(node.right)
    print(node)

print("Post-order DFS")
post_ord_dfs(root)
print("----------------------------------------")

#ITERATIVE APPROACH
def pre_iter_dfs(node):
    if not node:
        return
    stack =[node]

    while stack:
        curr = stack.pop()
        print(curr)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

print("Pre-order Iterative DFS")
pre_iter_dfs(root)

print("----------------------------------------")


#DFS search for a value in the tree
def search_dfs(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    return search_dfs(node.left, target) or search_dfs(node.right, target)
 



