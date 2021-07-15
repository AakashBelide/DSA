# 4 NSL | NEAREST SMALLER TO LEFT

arr = [4, 5, 2, 10, 8]

stack = []

ans = []

for i in range(len(arr)):
    if(len(stack) == 0):
        ans.append(-1)
    elif(stack[-1]<arr[i]):
        ans.append(stack[-1])
    else:
        while(len(stack)>0 and stack[-1]>arr[i]):
            stack.pop()
        if(len(stack) == 0):
            ans.append(-1)
        else:
            ans.append(stack[-1])
    stack.append(arr[i])

print(ans)