# Chocolate Distribution Problem
# https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1#

# Own Solution - Time Complexity: O(NLogN)
# Similar/same solution on GFG
def findMinDiff(A,N,M):
    A.sort()
    res = 99999999999
    for i in range(N-M+1):
        tmp = A[i+M-1] - A[i]
        if(tmp<res):
            res = tmp
    return res

N = 8
M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]

print(findMinDiff(A, N, M))