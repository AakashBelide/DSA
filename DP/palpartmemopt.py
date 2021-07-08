# Palindrome Partitioning Memoization
# https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/
# https://leetcode.com/problems/palindrome-partitioning-ii/

import sys
s = "nitik"

dp = [[-1 for i in range(len(s))] for j in range(len(s))]

def ispalindrome(s, i, j):
    if(i >= j):
        return True
    while i<j:
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True

def solve(s, i, j):
    if(i >= j or ispalindrome(s, i, j)):
        return 0
    
    if(dp[i][j] != -1):
        return dp[i][j]

    mn = sys.maxsize

    for k in range(i, j):
        if(dp[i][k] != -1):
            left = dp[i][k]
        else:
            left = solve(s, i, k)
            dp[i][k] = left
        
        if(dp[k+1][j] != -1):
            right = dp[k+1][j]
        else:
            right = solve(s, k+1, j)
            dp[k+1][j] = right
        
        temp = left + right + 1
        mn = min(temp, mn)
    dp[i][j] = mn
    return mn

print(solve(s, 0, len(s)-1))