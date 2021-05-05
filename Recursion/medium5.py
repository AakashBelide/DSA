#Permutations with case change

ip1 = input("Enter the lower case string: ")
ip2 = input("Enter the upper case string: ")
ip3 = input("Enter the any case string: ")
op = ""
x = []
y = []
z = []
#For only lower case input
def solve1(a, b, c):
    if (len(a) == 0):
        c.append(b)
        return
    else:
        b1 = b
        b2 = b
        b1 = b1 + a[0].upper()
        b2 = b2 + a[0]
        a = a[1:]
        solve1(a, b1, c)
        solve1(a, b2, c)
        return

#For only upper case input
def solve2(a, b, c):
    if (len(a) == 0):
        c.append(b)
        return
    else:
        b1 = b
        b2 = b
        b1 = b1 + a[0].lower()
        b2 = b2 + a[0]
        a = a[1:]
        solve2(a, b1, c)
        solve2(a, b2, c)
        return

#For any case input
def solve3(a, b, c):
    if (len(a) == 0):
        c.append(b)
        return
    else:
        b1 = b
        b2 = b
        if a[0].islower():
            b1 = b1 + a[0].upper()
            b2 = b2 + a[0].lower()
        else:
            b1 = b1 + a[0].lower()
            b2 = b2 + a[0].upper()
        a = a[1:]
        solve3(a, b1, c)
        solve3(a, b2, c)
        return

solve1(ip1, op, x)
solve2(ip2, op, y)
solve3(ip3, op, z)
print(x)
print(y)
print(z)