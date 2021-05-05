#printing 1 to N, N to 1 and factorial of N using recusrion

n = int(input("Enter the number: "))

#printing 1 to N using recusrion
def oneton(a):
    if (a == 1):
        print(a)
        return
    oneton(a-1)
    print(a)

#printing N to 1 using recusrion
def ntoone(b):
    if (b == 1):
        print(b)
        return
    print(b)
    ntoone(b-1)

#printing factorial of N using recusrion
def fact(c):
    if (c == 0 or c == 1):
        return 1
    return (c*fact(c-1))

print(fact(n))