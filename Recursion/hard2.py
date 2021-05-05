#Josephus Problem | Game of Death in a circle | Execution in Circle


#The total number of people present
n = [int(i) for i in range(1, int(input("Enter number of people: ")) + 1)]
#The number of people to skip after killing each person
k = int(input("Number of people to skip to kill: "))
k = k - 1
ind = 0

def sol(a, b, c):
    if (len(a) == 1):
        print(a[0])
        return
    print(a, b, c)
    c = (c + b) % len(a)
    a.remove(a[c])
    sol(a, b, c)

sol(n, k, ind)
