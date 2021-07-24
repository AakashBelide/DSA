# Merge Overlapping Subintervals
# https://leetcode.com/problems/merge-intervals/

# Time Complexity: O(nlogn), Space Complexity: O(n)

arr = [[1,3],[2,6],[8,10],[15,18]]

arr.sort()
pair = arr[0]
out = []

for i in arr:
    if(i[0]<=pair[1]):
        pair[1] = max(pair[1], i[1])
    else:
        out.append(pair)
        pair = i

out.append(pair)

print(out)