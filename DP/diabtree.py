# Diameter of a Binary Tree
# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1
# https://leetcode.com/problems/diameter-of-binary-tree/submissions/

import sys

def solve(root, res):
    if(root == None):
        return 0
    
    l = solve(root.left, res)
    r = solve(root.right, res)

    tmp = max(l, r) + 1
    # ans = max(tmp, 1+l+r) not required
    # res[0] = max(res[0], ans)
    res[0] = max(res[0], 1+l+r)

    return tmp

root = "some tree"

res = [-sys.maxsize - 1]

ans = solve(root, res)

print(res[0])