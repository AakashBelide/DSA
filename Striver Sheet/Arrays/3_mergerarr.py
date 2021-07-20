# Merge two sorted Arrays without extra space
# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1#
# 

# Time Complexity: O(n+m*(log(n+m))), Space Complexity: O(1)
# GAP Method, there is another approach in GFG editorial with TC O(n+m) and O(nm)

arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]

n = len(arr1)
m= len(arr2)

def n_gap(g):
    if(g<=1):
        return 0
    return (g//2) + (g%2)

gap = n + m
gap = n_gap(gap)

while gap>0:
    i = 0
    while i + gap<n:
        if(arr1[i]>arr1[i + gap]):
            arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
        i += 1
    
    j = gap-n if gap>n else 0
    while i<n and j<m:
        if(arr1[i]>arr2[j]):
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i += 1
        j += 1
    
    if(j<m):
        j = 0
        while j + gap<m:
            if(arr2[j]>arr2[j + gap]):
                arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
            j += 1
    
    gap = n_gap(gap)