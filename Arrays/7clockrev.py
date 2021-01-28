# Write a program to cyclically rotate an array by one.
# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1#

# GFG Approach Time Complexity: O(n)
def rotate( arr, n):
    a = arr[-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = a
    return arr

# Own approach if given array need not be changed by itself more space
def rotate2(arr):
    a = [arr[-1]] + arr[:-1]
    return a

ar = [1, 2, 3, 4, 5]

print(rotate2(ar))

print(rotate(ar, len(ar)))