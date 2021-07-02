# Matrix chain multiplication Memoization
# https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
import sys
arr = [40, 20, 30, 10, 30]

dp = [[-1 for i in range(len(arr))] for j in range(len(arr))]

def solve(arr, i, j):
    if(i==j):
        return 0

    if(dp[i][j] != -1):
        return dp[i][j]
    
    mn = sys.maxsize
    
    for k in range(i, j):
        temp = solve(arr, i, k) + solve(arr, k+1, j) + (arr[i-1] * arr[k] * arr[j])
        mn = min(temp, mn)
    
    dp[i][j] = mn
    return mn

print(solve(arr, 1, len(arr)-1))