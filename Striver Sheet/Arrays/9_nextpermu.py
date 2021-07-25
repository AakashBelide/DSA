# Next Permutation
# https://practice.geeksforgeeks.org/problems/next-permutation5226/1
# https://leetcode.com/problems/next-permutation/

# Time Complexity: O(n), Space Complexity: O(1)

arr = [1,2,3]

def nextPermutation(nums):
    i = len(nums) - 2
    while(i>=0 and nums[i+1]<=nums[i]):
        i-=1
    
    if(i>=0):
        j = len(nums) - 1
        while(j>=0 and nums[j]<=nums[i]):
            j-=1
        nums[i], nums[j] = nums[j], nums[i]
    def rev(nums1, start):
        i = start
        j = len(nums1)-1
        while(i<j):
            nums[i], nums1[j] = nums[j], nums1[i]
            i += 1
            j -= 1
    
    rev(nums, i+1)

nextPermutation(arr)
print(arr)