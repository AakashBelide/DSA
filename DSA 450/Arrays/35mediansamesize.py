# Median of 2 sorted arrays of equal size
# https://www.geeksforgeeks.org/median-of-two-sorted-arrays/

ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]

arr1 = [1, 2, 3, 6]
arr2 = [4, 6, 8, 10]

# GFG Solution
def getMedian( ar1, ar2 , n):
    i = 0 # Current index of i/p list ar1[]
     
    j = 0 # Current index of i/p list ar2[]
     
    m1 = -1
    m2 = -1
     
    # Since there are 2n elements, median
    # will be average of elements at index
    # n-1 and n in the array obtained after
    # merging ar1 and ar2
    count = 0
    while count < n + 1:
        count += 1
        if i == n:
            m1 = m2
            m2 = ar2[0]
            break
        elif j == n:
            m1 = m2
            m2 = ar1[0]
            break
        if ar1[i] <= ar2[j]:
            m1 = m2
            m2 = ar1[i]
            i += 1
        else:
            m1 = m2
            m2 = ar2[j]
            j += 1
    return (m1 + m2)/2

print(getMedian(ar1, ar2, len(ar1)))

print(getMedian(arr1, arr2, len(arr1)))