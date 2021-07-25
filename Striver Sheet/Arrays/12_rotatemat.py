# Rotate Matrix
# https://practice.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1# (Similar but -90 degree rorated)
# https://leetcode.com/problems/rotate-image/

# Time Complexity: O(n), Space Complexity: O(1)

mat = [[1,2,3],[4,5,6],[7,8,9]]

def rotate1(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
            
    return matrix
rotate1(mat)
print(mat)

def rotate2(matrix):
    n = len(matrix)
    for i in range(n//2):
        m = len(matrix[i]) - i - 1
        for j in range(i, m):
            tmp = matrix[m-j+i][i]
            matrix[m-j+i][i] = matrix[m][m-j+i]
            matrix[m][m-j+i] = matrix[j][m]
            matrix[j][m] = matrix[i][j]
            matrix[i][j] = tmp
    return matrix

rotate2(mat)
print(mat)