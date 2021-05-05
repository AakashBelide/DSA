#Reverse a stack using recursion

s = [int(i) for i in input("Enter the stack elements with spaces between each of them: ").split()]

def rev(a):
    if (len(a) == 1):
        return
    
    b = a.pop()
    rev(a)
    ins(a, b)
    return a

def ins(c, d):
    if (len(c) == 0):
        c.append(d)
        return
    
    e = c.pop()
    ins(c, d)
    c.append(e)
    return

print(rev(s))