A = [-5,-3,-2,-1,0,1,2,3,4,5]

def Search_b(A, target):
    left = 0
    right = len(A) - 1

    while left < right:
        Mid = left +((right - left)//2)
        if A[Mid] == target:
            return True
        elif A[Mid] > target:
            right = Mid - 1
        else:
            left = Mid + 1
    return False

result = Search_b(A, 0)
print(result)
            

