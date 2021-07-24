# Set Matrix Zeros
# https://practice.geeksforgeeks.org/problems/boolean-matrix-problem-1587115620/1# (Similar but here we need to set 1's)
# https://leetcode.com/problems/set-matrix-zeroes/

# Time Complexity: O(n*m), Space Complexity: O(1)

arr = [[1,1,1],[1,0,1],[1,1,1]]

def setZeroes(a):
    col = True
    n = len(a)
    m = len(a[0])
    for i in range(n):
        if(a[i][0] == 0):
            col = False
        for j in range(1, m):
            if(a[i][j] == 0):
                a[0][j] = 0
                a[i][0] = 0
    
    for i in range(n-1, -1, -1):
        for j in range(m-1, 0, -1):
            if(a[i][0] == 0 or a[0][j] == 0):
                a[i][j] = 0
        if(col == False):
            a[i][0] = 0

setZeroes(arr)

print(arr)