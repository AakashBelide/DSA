# 6 Stock Span Problem
# https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1

arr = [100, 80, 60, 70, 60, 75, 85]

stack = []

ans = []

for i in range(len(arr)):
    if(len(stack) == 0):
        ans.append(-1)
    elif(stack[-1][0]>arr[i]):
        ans.append(stack[-1][1])
    else:
        while(len(stack)>0 and stack[-1][0]<=arr[i]):
            stack.pop()
        if(len(stack) == 0):
            ans.append(-1)
        else:
            ans.append(stack[-1][1])
    stack.append([arr[i], i])

for i in range(len(ans)):
    ans[i] = i - ans[i]

""" No need of extra iteration
for i in range(len(arr)):
    if(len(stack) == 0):
        ans.append(i + 1)
    elif(stack[-1][0]>arr[i]):
        ans.append(i - stack[-1][1])
    else:
        while(len(stack)>0 and stack[-1][0]<=arr[i]):
            stack.pop()
        if(len(stack) == 0):
            ans.append(i+1)
        else:
            ans.append(i - stack[-1][1])
    stack.append([arr[i], i])"""

print(ans)