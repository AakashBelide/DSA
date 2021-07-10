# Egg Dropping Problem Recursive
# https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0
# https://leetcode.com/problems/super-egg-drop/

import sys

e = 3
f = 5

def solve(e, f):
    if(e == 1):
        return f

    if(f == 0 or f == 1):
        return f
    
    mn = sys.maxsize

    for i in range(1, f+1):
        temp = 1 + max(solve(e-1, i-1), solve(e, f-i))
        mn = min(mn, temp)
    
    return mn

print(solve(e, f))