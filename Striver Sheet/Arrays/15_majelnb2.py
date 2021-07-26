# Majority Element (>N/2 times)
# https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1#
# https://leetcode.com/problems/majority-element/

# Time Complexity: O(n), Space Complexity: O(1)

arr = [3,2,3]

def majorityElement(nums):
    c = 0
    el = -1
    for i in nums:
        if(c == 0):
            el = i
        if(el == i):
            c += 1
        else:
            c -= 1
    return el

print(majorityElement(arr))