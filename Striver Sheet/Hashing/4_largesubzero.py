# Largest Subarray with 0 sum
# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#

# Time Complexity: O(nlogn) or O(n), Space Complexity: O(n)

arr = [15,-2,2,-8,1,7,10,23]
n = len(arr)

def maxLen(n, arr):
    s = 0
    uni = {}
    mx = 0
    for i in range(n):
        s += arr[i]
        if(s == 0):
            mx = max(mx, i+1)
        if(s not in uni):
            uni[s] = i
        else:
            mx = max(mx, i - uni[s])
    return mx

print(maxLen(n, arr))