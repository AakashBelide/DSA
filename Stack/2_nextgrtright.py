# 2 NGR | Nearest Greater to right | Next Largest Element
# https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1
# https://leetcode.com/problems/next-greater-element-i/ (Similar - Extension)

arr = [1, 3, 2, 4]

stack = []

ans = []

for i in range(len(arr)-1, -1, -1):
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

ans.reverse()
print(ans)