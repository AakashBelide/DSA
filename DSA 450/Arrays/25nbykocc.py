# Given an array of size n and a number k, fin all elements that appear more than " n/k " times.
# https://www.geeksforgeeks.org/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/

# Hashing solution -  Time Complexity: O(N)
def nbykocc(arr, n, k):
    occ = {}

    for i in arr:
        if(i in occ):
            occ[i] += 1
        else:
            occ[i] = 1
    
    nk = []

    for i in occ:
        if(occ[i]>n//k):
            nk.append(i)
    
    return nk


# Other solutions on GFG

arr = [ 1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 3, 1, 3]
n = len(arr)
k = 4

print(n//k)

print(nbykocc(arr, n, k))