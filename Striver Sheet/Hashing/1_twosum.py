# 2 Sum problem
# https://practice.geeksforgeeks.org/problems/key-pair5616/1
# https://leetcode.com/problems/two-sum/

# Time Complexity: O(n), Space Complexity: O(n)

nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    uni = {}
    for i in range(len(nums)):
        diff = target-nums[i]
        if(diff in uni):
            return [uni[diff], i]
        else:
            uni[nums[i]] = i

print(twoSum(nums, target))