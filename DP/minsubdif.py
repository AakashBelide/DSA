# Minimum Subset Sum Difference
# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/

arr = [1, 2, 7]
sm = sum(arr)
n = len(arr)

dp = []
for i in range(n+1):
    a = []
    for j in range(sm+1):
        if(i==0 and j==0):
            a.append(True)
        elif(i==0):
            a.append(False)
        elif(j==0):
            a.append(True)
        else:
            if(arr[i-1]<=j):
                a.append(dp[i-1][j-arr[i-1]] or dp[i-1][j])
            else:
                a.append(dp[i-1][j])
    dp.append(a)

mn = 99999999

for i in range(sm//2):
    if(dp[-1][i] == True):
        mn = min(sm-2*i, mn)

print(mn)