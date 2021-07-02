# Minimum number of deletion in a string to make it a palindrome
# https://practice.geeksforgeeks.org/problems/minimum-deletitions1648/1


x = "agbcba"
y = x[::-1]
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

print(n - dp[n][m])