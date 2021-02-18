# Find if there is any subarray with sum equal to 0
# https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1

# GFG solution - Time Complexity: O(n)
def subArrayExists(arr,n):
    n_sum = 0
    s = set()
 
    for i in range(n):
        n_sum += arr[i]
 
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
 
    return False