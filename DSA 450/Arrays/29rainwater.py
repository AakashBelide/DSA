# Trapping Rain water problem
# https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1

# Left and right max - Time Complexity: O(N^2)
def trappingWater(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        left = arr[i]
        right = arr[i]
        l = i-1
        r = i+1
        while(l>=0):
            if(arr[l]>left):
                left = arr[l]
            l -= 1
        
        while(r<n):
            if(arr[r]>right):
                right = arr[r]
            r += 1
        res += min(left, right) - arr[i]
    return res

# Using 2 pointers - Time Complexity: O(N)
def trap(height):
    i = 0
    j = len(height)-1
    left_max = 0
    right_max = 0
    res = 0
    while(i<j):
        if(height[i]<height[j]):
            if(height[i]>=left_max):
                left_max = height[i]
            else:
                res += left_max - height[i]
            i+=1
        else:
            if(height[j]>=right_max):
                right_max = height[j]
            else:
                res += right_max - height[j]
            j-=1
    return res

arr = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trappingWater(arr))
print(trap(arr))