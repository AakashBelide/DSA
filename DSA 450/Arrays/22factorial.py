# Find factorial of a large number
# https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers/0

# Own solution using recursion
def fact(n):
    if(n == 0 or n ==1):
        return 1
    else:
        return fact(n-1)*n

# Own solution using while loop
def fact2(n):
    f = 1
    if(n == 0):
        return f
    while(n != 1):
        f = f*(n)
        n = n-1
    return f

"""n = int(input())

for i in range(n):
    print(fact(int(input())))"""