# Print Longest Common Subsequence
# https://www.geeksforgeeks.org/printing-longest-common-subsequence/

x = "abcdaf"
y = "acbcf"
x = "AGGTAB"
y = "GXTXAYB"
x = "ABCDGH"
y = "AEDFHR"
n = len(x)
m = len(y)

dp = []

"""
# More Time Consumed
for i in range(n+1):
    a = []
    for j in range(m+1):
        if(i==0 or j==0):
            a.append("")
        else:
            if(x[i-1] == y[j-1]):
                a.append(dp[i-1][j-1] + x[i-1])
            else:
                if(len(dp[i-1][j])> len(a[j-1])):
                    tmp_mx = dp[i-1][j]
                else:
                    tmp_mx = a[j-1]
                a.append(tmp_mx)
    dp.append(a)

#print(dp)
print(dp[n][m])

# More Memory Consumed
for i in range(n+1):
    a = []
    for j in range(m+1):
        if(i==0 or j==0):
            a.append([0, ""])
        else:
            if(x[i-1] == y[j-1]):
                a.append([1 + dp[i-1][j-1][0], dp[i-1][j-1][1] + x[i-1]])
            else:
                if(dp[i-1][j][0]> a[j-1][0]):
                    tmp_mx = [dp[i-1][j][0], dp[i-1][j][1]]
                else:
                    tmp_mx = [a[j-1][0], a[j-1][1]]
                a.append(tmp_mx)
    dp.append(a)
#print(dp)
print(dp[n][m][1])"""
