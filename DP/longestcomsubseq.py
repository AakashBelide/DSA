# Longest Common Subsequence Top Down
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# https://leetcode.com/problems/longest-common-subsequence/

x = "abcdaf"
y = "acbcf"
n = len(x)
m = len(y)

dp = []

for i in range(n+1):
    a = []
    for j in range(m+1):
        if(i==0 or j==0):
            a.append(0)
        else:
            if(x[i-1] == y[j-1]):
                a.append(1 + dp[i-1][j-1])
            else:
                a.append(max(dp[i-1][j], a[j-1]))
    dp.append(a)

print(dp[n][m])