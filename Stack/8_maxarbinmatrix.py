# 8 Max Area Rectangle in binary matrix
# https://practice.geeksforgeeks.org/problems/max-rectangle/1# (TLE)

mat = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]

def mah(arr):
    # Left traversal
    stack = []

    left = []

    for i in range(len(arr)):
        if(len(stack) == 0):
            left.append(-1)
        elif(stack[-1][0]<arr[i]):
            left.append(stack[-1][1])
        else:
            while(len(stack)>0 and stack[-1][0]>=arr[i]):
                stack.pop()
            if(len(stack) == 0):
                left.append(-1)
            else:
                left.append(stack[-1][1])
        stack.append([arr[i], i])

    # Right traversal
    stack = []

    right = []

    for i in range(len(arr)-1, -1, -1):
        if(len(stack) == 0):
            right.append(len(arr))
        elif(stack[-1][0]<arr[i]):
            right.append(stack[-1][1])
        else:
            while(len(stack)>0 and stack[-1][0]>=arr[i]):
                stack.pop()
            if(len(stack) == 0):
                right.append(len(arr))
            else:
                right.append(stack[-1][1])
        stack.append([arr[i], i])
    right.reverse()

    ans = 0

    for i in range(len(arr)):
        tmp = right[i] - left[i] - 1
        ans = max(ans, tmp*arr[i])
    
    return ans

stck = []

for j in range(len(mat)):
    stck.append(mat[0][j])

mx = mah(stck)

for i in range(1, len(mat)):
    for j in range(len(mat[i])):
        if(mat[i][j] == 0):
            stck[j] = 0
        else:
            stck[j] += mat[i][j]
    mx = max(mx, mah(stck))

print(mx)
