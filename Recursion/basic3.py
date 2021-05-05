#Deleting middle element in a stack using recursion

s = [int(i) for i in input("Enter the stack elements with spaces between each of them: ").split()]
l = len(s)
def delmid(a, b):
    if (b == 0):
        return a
    
    k = ((b/2) + 1)
    """
    if (b%2 == 0):
        k = ((b/2) + 1)
    else:
        k = ((b+1)/2)
    """
    solve(a, int(k))
    return a

def solve(c, d):
    if (d == 1):
        c.pop()
        return
    
    temp = c.pop()
    solve(c, d-1)
    c.append(temp)
    return

print(delmid(s,l))