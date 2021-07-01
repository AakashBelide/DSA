# Longest Common Substring
# https://www.geeksforgeeks.org/longest-common-substring-dp-29/
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/ (Similar but with number array)

x = "abcdaf"
y = "acbcf"
#x = "abcijkl"
#y = "ijklabc"
n = len(x)
m = len(y)

dp = []
mx = 0
for i in range(n+1):
    a = []
    for j in range(m+1):
        if(i==0 or j==0):
            a.append(0)
        else:
            if(x[i-1] == y[j-1]):
                tmp = 1 + dp[i-1][j-1]
                a.append(tmp)
                mx = max(mx, tmp)
            else:
                a.append(0)
    dp.append(a)

#print(dp)
print(mx)