# 7 Maximum Area Histogram | MAH
# https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1# (TLE)
# https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/

arr = [6, 2, 5, 4, 5, 1, 6]

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

# print(left)
# print(right)

print(ans)