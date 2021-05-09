# 0-1 Knapsack Memoization

wt = [1,3,4,5]
val = [1,4,5,7]
w = 7
n = len(wt)

dp = []
for i in range(w+1):
    a = []
    for j in range(n+1):
        a.append(-1)
    dp.append(a)

def knapsack(wt, val, w, n, dp):
    if(n == 0 or w == 0):
        return 0
    if(dp[w][n]!=-1):
        return dp[w][n]
    if(wt[n-1]<=w):
        dp[w][n] = max(val[n-1] + knapsack(wt, val, w-wt[n-1], n-1, dp), knapsack(wt, val, w, n-1, dp))
        return dp[w][n]
    else:
        dp[w][n] = knapsack(wt, val, w, n-1, dp)
        return dp[w][n]

print(knapsack(wt, val, w, n, dp))