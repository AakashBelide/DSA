# Repeat and Missing Number
# https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1#


# Time Complexity: O(n), Space Complexity: O(n)

arr = [1, 3, 3]
n = len(arr)

uni = {}
s = 0
r = -1
org_s = int((n*(n+1))/2)
for i in arr:
    if i not in uni:
        uni[i] = 1
    else:
        uni[i] += 1
        r = i
    s += i

print([r, (r - (s - org_s))])