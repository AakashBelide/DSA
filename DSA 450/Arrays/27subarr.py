# Find whether an array is a subset of another arra
# https://practice.geeksforgeeks.org/problems/array-subset-of-another-array/0#

# Own solution - Time Complexity: O(MN)
def sub(arr1, arr2, l2):
    count = 0
    for k in range(l2):
        if(arr2[k] in arr1):
            count += 1
    if(l2 == count):
        return "Yes"
    else:
        return "No"

# Own Solution 2 using Hashing - Time complexit: O(M+N)
def sub2(arr1, arr2, l1, l2):
    ar1 = {}
    ar2 = {}
    for j in range(l1):
        if(arr1[j] in ar1):
            ar1[arr1[j]] += 1
        else:
            ar1[arr1[j]] = 1
    
    for k in range(l2):
        if(arr2[k] in ar2):
            ar2[arr2[k]] += 1
        else:
            ar2[arr2[k]] = 1
    
    count = 0
    
    for l in ar2:
        if(l in ar1 and ar1[l]>=ar2[l]):
            count += 1
    
    if(l2 == count):
        return "Yes"
    else:
        return "No"