# Majority Element (>N/3 times)
# https://www.geeksforgeeks.org/n3-repeated-number-array-o1-space/
# https://leetcode.com/problems/majority-element-ii/

# Time Complexity: O(n), Space Complexity: O(1)

arr = [3,2,3]

def majorityElement(nums):
    n = len(nums)
    c1 = 0
    c2 = 0
    el1 = -1
    el2 = -1
    for i in range(n):
        if(nums[i] == el1):
            c1 += 1
        elif(nums[i] == el2):
            c2 += 1
        elif(c1 == 0):
            c1 = 1
            el1 = nums[i]
        elif(c2 == 0):
            c2 = 1
            el2 = nums[i]
        else:
            c1 -= 1
            c2 -= 1
    out = []
    ct1 = 0
    ct2 = 0
    for i in range(n):
        if(nums[i] == el1):
            ct1 += 1
        elif(nums[i] == el2):
            ct2 += 1
    if(ct1>(n/3)):
        out.append(el1)
    
    if(ct2>(n/3)):
        out.append(el2)
    
    return out

print(majorityElement(arr))