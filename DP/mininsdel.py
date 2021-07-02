# Minimum Number of Insertion and Deletion to convert String a to String b
# https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1#
# https://leetcode.com/problems/delete-operation-for-two-strings/

x = "heap"
y = "pea"
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

print("Inserted: " + str(m - dp[n][m]) + ", Deleted: " + str(n - dp[n][m]))