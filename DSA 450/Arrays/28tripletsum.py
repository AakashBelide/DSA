# Find the triplet that sum to a given value
# https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1

# GFG Sollution using Hashing - Time Complexity: O(N^2)
def find3Numbers(arr, N, X):
    for i in range(N):
        s = set() 
        curr_sum = X - arr[i] 
        for j in range(i + 1, N): 
            if (curr_sum - arr[j]) in s: 
                return True
            s.add(arr[j])