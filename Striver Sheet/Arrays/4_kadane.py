# Kadane’s Algorithm
# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1#
# https://leetcode.com/problems/maximum-subarray/

# Time Complexity: O(n), Space Complexity: O(1)

arr = [1,2,3,-2,5]

mx = -9999999
tmp = 0
for i in arr:
    tmp += i
    mx = max(mx, tmp)
    if(tmp<0):
        tmp = 0
print(mx)