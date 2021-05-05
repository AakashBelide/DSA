#Tower of Hanoi with each step printed along with number of steps printed

n = int(input("Enter your number: "))
count = 0
x = "Source"
y = "Auxillary"
z = "Destination"
def sol(m, s, d, h, c):
    if (m == 1):
        print("Moved plate " + str(m) + " from " + s + " to " + d)
        c+=1
        return c
    
    sol(m-1, s, h, d, c)
    print("Moved plate " + str(m) + " from " + s + " to " + d)
    c+=1
    sol(m-1, h, d, s, c)
    return c

print(sol(n, x, z, y, count))