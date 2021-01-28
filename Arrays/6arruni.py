# Find the Union and Intersection of the two sorted arrays.
# https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1

# Own Solution

def doUnion(a,n,b,m):
    c = []
    for i in range(n):
        if(a[i] not in c):
            c.append(a[i])
    for j in range(m):
        if(b[j] not in c):
            c.append(b[j])
    return len(c)

a = [85, 25, 1, 32, 54, 6]
b = [85, 2]
n = 6
m = 2

print(doUnion(a,n,b,m))
