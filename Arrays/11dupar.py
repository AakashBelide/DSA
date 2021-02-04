# find duplicate in an array of N+1 Integers
# https://leetcode.com/problems/find-the-duplicate-number/

def findDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if(nums[i] == nums[i+1]):
            return(nums[i])

nums = [1,3,4,2,2]

print(findDuplicate(nums))

# Other solution reference: https://www.youtube.com/watch?v=32Ll35mhWg0&t=383s