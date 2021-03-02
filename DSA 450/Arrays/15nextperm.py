# Next Permutation
# https://leetcode.com/problems/next-permutation/

# Leetcode solution - Time complexity: O(n)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
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