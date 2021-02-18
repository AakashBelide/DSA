# Rearrange the array in alternating positive and negative items with O(1) extra space
# https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/

# Own solution - Time Complexity: O(n)
def altnegpos(arr):
    arr.sort()
    n = 0
    for i in range(len(arr)):
        if(arr[i]>=0):
            n = i
            break
    
    for i in range(len(arr)):
        if((i+1)%2 == 0 and arr[i]<0):
            arr[i], arr[n] = arr[n], arr[i]
            n += 1

#GFG Solution - Time Complexit: O(n)
def rightRotate(arr, n, outOfPlace, cur):
    temp = arr[cur]
    for i in range(cur, outOfPlace, -1):
        arr[i] = arr[i - 1]
    arr[outOfPlace] = temp
    return arr
 
 
def rearrange(arr, n):
    outOfPlace = -1
    for index in range(n):
        if(outOfPlace >= 0):
            if((arr[index] >= 0 and arr[outOfPlace] < 0) or
               (arr[index] < 0 and arr[outOfPlace] >= 0)):
                arr = rightRotate(arr, n, outOfPlace, index)
                if(index-outOfPlace > 2):
                    outOfPlace += 2
                else:
                    outOfPlace = - 1
 
        if(outOfPlace == -1):
            if((arr[index] >= 0 and index % 2 == 0) or
               (arr[index] < 0 and index % 2 == 1)):
                outOfPlace = index
    return arr

#ar = [1, 2, 3, -4, -1, 4]

ar = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

altnegpos(ar)

print(ar)