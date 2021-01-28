# Move all the negative elements to one side of the array 
# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/


# Partition process of quicksort Time complexity: O(N)
def negmov(arr):
    a = 0
    for i in range(len(arr)):
        if(arr[i]<0):
            temp = arr[a]
            arr[a] = arr[i]
            arr[i] = temp
            a += 1
        print(arr)
    return arr

# Left and right pointer approach Time Complexity: O(N)
def negmov2(arr):
    l = 0
    r = len(arr) - 1
    while(l<=r):
        if(arr[l]<0 and arr[r]<0):
            l += 1
        elif(arr[l]>0 and arr[r]>0):
            r -= 1
        elif(arr[l]>0 and arr[r]<0):
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1
            r -= 1
        else:
            l += 1
            r -= 1
    return arr

# Own Approach 1 - More memory consumption

def negmov3(arr):
    a = []
    b = []
    for i in range(len(arr)):
        if(arr[i]<0):
            a.append(arr[i])
        else:
            b.append(arr[i])
    return(a+b)


# Own Approach 2 - Using inbuilt sort function
def negmov4(arr):
    arr.sort()
    return arr

ar = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

print(negmov4(ar))