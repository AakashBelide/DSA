# Print shortest common Supersequence
#

x = "abcdaf"
y = "acbcf"

x = "abac"
y = "cab"

n = len(x)
m = len(y)

dp = []

for i in range(n+1):
    a = []
    for j in range(m+1):
        if(i==0):
            a.append([j, ""])
        elif(j==0):
            a.append([i, ""])
        else:
            if(x[i-1] == y[j-1]):
                a.append([1 + dp[i-1][j-1][0], dp[i-1][j-1][1] + x[i-1]])
            else:
                if(dp[i-1][j][0]> a[j-1][0]):
                    tmp_mx = [dp[i-1][j][0], dp[i-1][j][1] + x[i-1]]
                else:
                    tmp_mx = [a[j-1][0], a[j-1][1] + y[j-1]]
                a.append(tmp_mx)
    dp.append(a)

print(dp)

print(dp[n][m][1])