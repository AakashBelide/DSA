# Find the duplicate in an array of N+1 integers.
# https://leetcode.com/problems/find-the-duplicate-number/

# Time Complexity: O(n), Space Complexity: O(1)

arr = [1,3,4,2,2]

def findDuplicate1(nums):
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if(slow == fast):
            break
    
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow


# Time Complexity: O(nlogn), Space Complexity: O(1) but here we are modifying the array

def findDuplicate2(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if(nums[i] == nums[i+1]):
            return(nums[i])

print(findDuplicate1(arr))
print(findDuplicate2(arr))