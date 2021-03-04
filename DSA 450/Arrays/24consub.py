# Find longest coinsecutive subsequence
# https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1

# Own Solution - Time Complexit: O(NlogN)
def findLongestConseqSubseq(arr, N):
    arr.sort()
    arr1 = list(set(arr))
    mx = 1
    temp = 1
    for i in range(len(arr1)-1):
        if(arr1[i+1]-arr1[i]==1):
            temp += 1
        else:
            temp = 1
        if(temp>mx):
            mx = temp
    return mx

arr = [1,9,3,10,4,20,2]
n = len(arr)

# Own Solution based on GFG - Time Complexity: O(N)
def findLongestConseqSubseq2(arr, N):
    arr1 = set(arr)
    mx = 1
    for i in arr1:
        temp = 1
        while i+1 in arr1:
            temp += 1
            i += 1
        if(temp>mx):
            mx = temp
    return mx

# Other GFG solutions: https://www.geeksforgeeks.org/longest-consecutive-subsequence/

arr = [1,9,3,10,4,20,2]
arr = [3, 7, 10, 12, 4, 39, 80, 5, 12, 10, 8, 3, 6, 7, 9, 11]
n = len(arr)

print(findLongestConseqSubseq(arr, n))
print(findLongestConseqSubseq2(arr, n))