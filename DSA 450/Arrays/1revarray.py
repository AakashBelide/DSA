# Reverse the array
# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

a = [4, 7, 2, 8, 5, 1]
b = [7, 2, 4, 0, 1, 5, 7]

# Using Python list slicing
print(b[::-1])

# GFG Iterative solution
# Time Complexity : O(n)
def revar(arr):
    start = 0
    end = len(arr) - 1
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr

# Here the list/array is passed itself so it changes after executing this
print(revar(b))

# There is another solution using Recursive approach which has same Time Complexity : O(n)