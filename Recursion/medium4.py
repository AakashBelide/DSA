#Permutations with spaces

ip = input("Enter the string you want permutations with spaces for: ")
op = ""
op = ip[0]
ip = ip[1:]
x = []

def solve(a, b):
    if (len(a) == 0):
        x.append(b)
        return
    else:
        b1 = b
        b2 = b
        b1 = b1 + " " + a[0]
        b2 = b2 + a[0]
        a = a[1:]
        solve(a, b1)
        solve(a, b2)
        return

solve(ip, op)
x.sort()
print(x)