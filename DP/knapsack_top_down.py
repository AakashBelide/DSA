# 0-1 Knapsack Top-Down

wt = [1,3,4,5]
val = [1,4,5,7]
w = 7
n = len(wt)

dp = []
for i in range(n+1):
    a = []
    for j in range(w+1):
        if(i==0 or j==0):
            a.append(0)
        else:
            if(wt[i-1]<=j):
                a.append(max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j]))
            else:
                a.append(dp[i-1][j])
    dp.append(a)

"""for i in range(1, n+1):
    for j in range(1, w+1):
        if(wt[i-1]<=j):
            dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]"""

#print(dp)
print(dp[n][w])