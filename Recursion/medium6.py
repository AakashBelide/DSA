#Letter case change

ip = input("Enter the string you want permutations with spaces for: ")
op = ""
x = []

def solve(a, b, c):
    if (len(a) == 0):
        c.append(b)
        return
        
    if a[0].isalpha():
        b1 = b
        b2 = b
        b1 = b1 + a[0].lower()
        b2 = b2 + a[0].upper()
        a = a[1:]
        solve(a, b1, c)
        solve(a, b2, c)
        return
    else:
        b = b + a[0]
        a = a[1:]
        solve(a, b, c)
        return
        

solve(ip, op, x)
print(x)