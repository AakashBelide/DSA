# find all pairs on integer array whose sum is equal to given number 	
# https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

# GFG Solution - Time Complexity: O(n)
def getPairsCount(self, arr, n, k):
    m = [0] * 10000000
    for i in arr:
        m[i] += 1
    c = 0
    for i in arr:
        c += m[k - i]
        
        if(k - i == i):
            c -= 1
    return int(c/2)

# Own Solution - Time Complexity: O(n^2)
def getPairsCount2(self, arr, n, k):
    c = 0
    for i in range(n):
        x = k - arr[i]
        c += arr[i+1:].count(x)
    return c