# Merge Intervals
# https://leetcode.com/problems/merge-intervals/

def merge(intervals):
    intervals.sort()
    a = []
    a.append(intervals[0])
    j = 0
    for i in range(1, len(intervals)):
        if(intervals[i][0]<=a[j][1]):
            a[j][0] = min([intervals[i][0], a[j][0]])
            a[j][1] = max([intervals[i][1], a[j][1]])
        else:
            a.append(intervals[i])
            j += 1
    return a

def merge2(intervals):
    intervals.sort()
    i = 0
    while(i<len(intervals)-1):
        #print(intervals, i)
        if(intervals[i][1]>=intervals[i+1][0]):
            intervals[i][0] = min([intervals[i][0], intervals[i+1][0]])
            intervals[i][1] = max([intervals[i][1], intervals[i+1][1]])
            intervals.pop(i+1)
            i -= 1
        i += 1
    return intervals

ar = [[1,3],[2,6],[8,10],[15,18]]
#ar = [[1,4],[4,5]]

print(merge2(ar))
