# Longest Consecutive Sequence
# https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1#
# https://leetcode.com/problems/longest-consecutive-sequence/

# Time Complexity: O(n), Space Complexity: O(n) - Striver Approach but slower

nums = [100,4,200,1,3,2]

def longestConsecutive1(nums):
    uni = {}
    n = len(nums)
    for i in range(n):
        if(nums[i] not in uni):
            uni[nums[i]] = 1
    mx = 0
    for i in range(n):
        if(nums[i]-1 not in uni):
            c = 0
            tmp = nums[i]
            while tmp in uni:
                c += 1
                tmp += 1
            mx = max(mx, c)
    
    return mx

# Time Complexity: O(nlogn), Space Complexity: O(n) - Own Approach but faster

def longestConsecutive2(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    nums2 = list(sorted(set(nums)))
    ans = 1
    tmp = 1
    for i in range(1, len(nums2)):
        if(nums2[i]-nums2[i-1] == 1):
            tmp += 1
        else:
            tmp = 1
        ans = max(tmp, ans)
    return ans

print(longestConsecutive1(nums))
print(longestConsecutive2(nums))