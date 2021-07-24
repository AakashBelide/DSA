# Pascal Triangle
# https://practice.geeksforgeeks.org/problems/pascal-triangle0652/1# (Similar but return only row)
# https://leetcode.com/problems/pascals-triangle-ii/ (Similar but return only row)
# https://leetcode.com/problems/pascals-triangle/

# Time Complexity: O(n), Space Complexity: O(n)

n = 4

def getRow1(n):
    arr = []
    j = 0
    k = n
    for i in range(n+1):
        if(i == 0 or i == n):
            arr.append(1)
        else:
            tmp = (arr[-1]*(k))//j
            arr.append(tmp)
            k -= 1
        j += 1
    return arr



# Time Complexity: O(n^2), Space Complexity: O(n^2)

def getRow2(n):
    arr = []
    for i in range(n+1):
        tmp = []
        for j in range(i+1):
            if(j == 0 or j == i):
                tmp.append(1)
            else:
                sm = arr[-1][j] + arr[-1][j-1]
                tmp.append(sm)
        arr.append(tmp)
    return arr[-1]

print(getRow1(n))
print(getRow2(n))