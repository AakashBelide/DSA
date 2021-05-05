#Generate all balanced Parentheses

n = int(input("Enter number: "))

o = n
c = n
op = ""
a = []


def sol(w, x , y, z):
    if (w==0 and x ==0):
        z.append(y)
        return
    
    if (w!=0):
        op1 = y
        op1 += "("
        sol(w-1, x, op1, z)
    
    if (x > w):
        op2 = y
        op2 += ")"
        sol(w, x-1, op2, z)
    
    return

sol(o, c, op, a)

print(a)