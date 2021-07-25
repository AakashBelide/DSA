# Search in a 2D matrix
# https://practice.geeksforgeeks.org/problems/search-in-a-matrix17201720/1#
# https://leetcode.com/problems/search-a-2d-matrix/
# https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/ (Similar to GFG problem)

arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
n = len(arr)
m = len(arr[0])
target = 3

# Time Complexity: O(log(nm)), Space Complexity: O(1)
def searchMatrix(matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        
        lo = 0
        high = n*m - 1
        
        while lo<=high:
            mid = (lo+high)//2
            if(matrix[mid//m][mid%m] == target):
                return True
            if(matrix[mid//m][mid%m] < target):
                lo = mid + 1
            else:
                high = mid - 1
        
        return False

print(searchMatrix(arr, target))


# Time Complexity: O(n + m), Space Complexity: O(1)
def matSearch(mat, N, M, X):
    res = 0
    
    i = 0
    j = M - 1
    
    while i<N and j>=0:
        if(mat[i][j] == X):
            res = 1
            return res
        if(mat[i][j]<X):
            i += 1
        else:
            j -= 1
    return res

print(matSearch(arr, n, m, target))