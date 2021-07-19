# 9 Rain Water Trapping
# https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1
# https://leetcode.com/problems/trapping-rain-water/

arr = [3, 0, 0, 2, 0, 4]

l2r = []
l2r.append(arr[0])

r2l = []
r2l.append(arr[-1])

n = len(arr)

for i in range(1, n):
    l2r.append(max(l2r[i-1], arr[i]))

j = 0

for i in range(n-2, -1, -1):
    r2l.append(max(r2l[j], arr[i]))
    j += 1

r2l.reverse()

amount = 0

for i in range(n):
    amount += min(l2r[i], r2l[i]) - arr[i]

print(amount)