class node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    

head = node(1)
A = node(2)
B = node(3)
C = node(4) 

head.next = A
A.next = B 
B.next = C

print(head)

curr = head
while curr:
    print(curr)
    curr = curr.next