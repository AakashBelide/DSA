# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

def sort012(arr,n):
    a = []
    for i in range(n):
        if(arr[i] == 0):
            a.append(arr[i])
    for i in range(n):
        if(arr[i] == 1):
            a.append(arr[i])
    for i in range(n):
        if(arr[i] == 2):
            a.append(arr[i])
    return a
    #for i in range(n):
        #arr[i] = a[i]
        

n = 5
a = [0, 2, 1, 2, 0]

print(sort012(a, n))

def sort2012(arr,n):
    z = 0
    o = 0
    t = 0
    a = []
    for i in range(n):
        if(arr[i] == 0):
            z += 1
        if(arr[i] == 1):
            o += 1
        if(arr[i] == 2):
            t += 1
    a = z*[0] + o*[1] + t*[2]
    return a

print(sort2012(a, n))