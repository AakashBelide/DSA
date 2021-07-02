# Print shortest common Supersequence
#

x = "abcdaf"
y = "acbcf"

x = "abac"
y = "cab"

n = len(x)
m = len(y)

dp = []

for i in range(n + 1):
    a = []
    for j in range(m + 1):
        if i == 0:
            a.append(j)
        elif j == 0:
            a.append(i)
        elif x[i - 1] == y[j - 1]:
            a.append(1 + dp[i - 1][j - 1])
        else:
            a.append(1 + min(dp[i - 1][j], a[j - 1]))
    dp.append(a)

st = ""

while n > 0 and m > 0:
    if x[n - 1] == y[m - 1]:
        st = x[n - 1] + st
        n -= 1
        m -= 1
    elif dp[n - 1][m] > dp[n][m - 1]:
        st = y[m - 1] + st
        m -= 1
    else:
        st = x[n - 1] + st
        n -= 1

while n > 0:
    st = x[n - 1] + st
    n -= 1

while m > 0:
    st = y[m - 1] + st
    m -= 1

print(st)