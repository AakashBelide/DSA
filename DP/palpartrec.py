# Palindrome Partitioning Recursive
# https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/
# https://leetcode.com/problems/palindrome-partitioning-ii/

import sys
s = "nitik"

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

    mn = sys.maxsize

    for k in range(i, j):
        temp = solve(s, i, k) + solve(s, k+1, j) + 1
        mn = min(temp, mn)
    
    return mn

print(solve(s, 0, len(s)-1))