# Sort an array of 0’s 1’s 2’s without using extra space or sorting algo
# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
# https://leetcode.com/problems/sort-colors/

# Time Complexity: O(n), Space Complexity: O(1)

arr = [2,0,2,1,1,0]

lo = 0
hi = len(arr) - 1
mid = 0

while mid<=hi:
    if(arr[mid] == 0):
        arr[lo], arr[mid] = arr[mid], arr[lo]
        lo += 1
        mid += 1
    elif(arr[mid] == 1):
        mid += 1
    elif(arr[mid] == 2):
        arr[mid], arr[hi] = arr[hi], arr[mid]
        hi -= 1

print(arr)