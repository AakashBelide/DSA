# 3 NGL | Nearest Greater to left

arr = [1, 3, 2, 4]

stack = []

ans = []

for i in range(len(arr)):
    if(len(stack) == 0):
        ans.append(-1)
    elif(stack[-1]>arr[i]):
        ans.append(stack[-1])
    else:
        while(len(stack)>0 and stack[-1]<arr[i]):
            stack.pop()
        if(len(stack) == 0):
            ans.append(-1)
        else:
            ans.append(stack[-1])
    stack.append(arr[i])

print(ans)