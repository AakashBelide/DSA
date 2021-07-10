# Egg Dropping Problem Memoization Optimized
# https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0
# https://leetcode.com/problems/super-egg-drop/

# Gives TLE for Python code on Leetcode and GFG but runs with Java code on GFG but not Leetcode

import sys

e = 3
f = 5

dp = [[-1]*(f+1) for _ in range(e+1)]

def solve(e, f):
    if(e == 1):
        return f

    if(f == 0 or f == 1):
        return f

    if(dp[e][f] != -1):
        return dp[e][f]
    else:
        mn = sys.maxsize

        for i in range(1, f+1):
            # for broken scenario
            if(dp[e-1][i-1] != -1):
                broken = dp[e-1][i-1]
            else:
                broken = solve(e-1, i-1)
                dp[e-1][i-1] = broken
            
            # for not broken scenario
            if(dp[e][f-i] != -1):
                n_broken = dp[e][f-i]
            else:
                n_broken = solve(e, f-i)
                dp[e][f-i] = n_broken
            
            temp = 1 + max(broken, n_broken)
            mn = min(mn, temp)
        
        dp[e][f] = mn
        return mn

print(solve(e, f))