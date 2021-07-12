# Maximum Path Sum | From leaf node to leaf node
# https://practice.geeksforgeeks.org/problems/maximum-path-sum/1

import sys

def solve(root, res):
    if(root == None):
        return 0
    
    l = solve(root.left, res)
    r = solve(root.right, res)

    if(root.left != None and root.right != None):
        tmp = max(l, r) + root.val
        res[0] = max(res[0], l + r + root.val)
        return tmp
    
    if(root.left == None):
        return r + root.val
    elif(root.right == None):
        return l + root.val

root = "some tree"

res = [-sys.maxsize - 1]

ans = solve(root, res)

print(res[0])