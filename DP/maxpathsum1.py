# Maximum Path Sum | From any node to any node
# https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

import sys

def solve(root, res):
    if(root == None):
        return 0
    
    l = solve(root.left, res)
    r = solve(root.right, res)

    tmp = max(max(l, r) + root.val, root.val)
    ans = max(tmp, l + r + root.val)
    res[0] = max(res[0], ans)

    return tmp

root = "some tree"

res = [-sys.maxsize - 1]

ans = solve(root, res)

if(res[0]==(-sys.maxsize - 1)):
    print(ans)

print(res[0])