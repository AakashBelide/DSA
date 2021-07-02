# Longest repeating subsequence
# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1

x = "aabebcdd"
n = len(x)
m = len(x)

dp = []

for i in range(n+1):
    a = []
    for j in range(m+1):
        if(i==0 or j==0):
            a.append(0)
        else:
            if(x[i-1] == x[j-1] and i != j):
                a.append(1 + dp[i-1][j-1])
            else:
                a.append(max(dp[i-1][j], a[j-1]))
    dp.append(a)

print(dp[n][m])