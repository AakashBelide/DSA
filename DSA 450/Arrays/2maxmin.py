# Find the maximum and minimum element in an array
# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

# Simple Linear Search
# Time Complexity: O(n)

def minmax(arr):
    l = len(arr)

    if(l == 1):
        return("Minimum: " + str(arr[0]) + ", Maximum: " + str(arr[0]))
    else:
        if(arr[0]>arr[1]):
            mini = arr[1]
            maxi = arr[0]
        else:
            mini = arr[0]
            maxi = arr[1]
        for i in range(2, l):
            if(arr[i] > maxi):
                maxi = arr[i]
            if(arr[i] < mini):
                mini = arr[i]
        return("Minimum: " + str(mini) + ", Maximum: " + str(maxi))

a = [1000, 11, 445, 7, 330, 3000]

print(minmax(a))

''' There are other solutions using Tournament Method in which the array is split into 2 parts and the minimum and maximum is
found for each part. Apart from that, there is another solution in which the minimum and maximum is checked in pairs by first
initializing min and max with starting 2 elements if there are even number of elements and then compared in pairs or intialise
min and max with first element if there are odd number of elements and then compared in pairs. All these methos have same 
time complexity of O(n). '''

# Own solution
def minmax2(arr):
    arr.sort()
    return("Minimum: " + str(arr[0]) + ", Maximum: " + str(arr[-1]))

print(minmax2(a))