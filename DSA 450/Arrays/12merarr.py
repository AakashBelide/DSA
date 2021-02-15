# Merge 2 sorted arrays without using Extra space.
# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1#

# Own solution but not proper memory space
def merge(arr1, arr2, n, m): 
    arr1.extend(arr2)
    arr1.sort()
    for i in range(m):
        arr2[i] = arr1[n]
        arr1.pop(n)
    return

n = 4
m = 5
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]

merge(arr1, arr2, n, m)

for x in arr1:
    print(x, end = " ")

for x in arr2:
    print(x, end = " ")