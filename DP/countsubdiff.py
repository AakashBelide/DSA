# Count number of Subset with given Difference

arr = [1, 1, 2, 3]
df = 1
n = len(arr)
def subsetdiff(arr, n, df):
    sm = (df+sum(arr))/2
    if(sm == int(sm)):
        sm = int(sm)
    else:
        return 0

    dp = []
    for i in range(n+1):
        a = []
        for j in range(sm+1):
            if(i==0 and j==0):
                a.append(1)
            elif(i==0):
                a.append(0)
            elif(j==0):
                a.append(1)
            else:
                if(arr[i-1]<=j):
                    a.append(dp[i-1][j-arr[i-1]] + dp[i-1][j])
                else:
                    a.append(dp[i-1][j])
        dp.append(a)

    return dp[n][sm]

print(subsetdiff(arr, n, df))