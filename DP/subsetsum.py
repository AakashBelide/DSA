# Subset Sum
# https://practice.geeksforgeeks.org/problems/subset-sum-problem2014
arr = [2, 3, 7, 8, 10]
sm = 11
n = len(arr)

dp = []
for i in range(n+1):
    a = []
    for j in range(sm+1):
        if(i==0 and j==0):
            a.append(True)
        elif(i==0):
            a.append(False)
        elif(j==0):
            a.append(True)
        else:
            if(arr[i-1]<=j):
                a.append(dp[i-1][j-arr[i-1]] or dp[i-1][j])
            else:
                a.append(dp[i-1][j])
    dp.append(a)

"""for i in range(n+1):
    st = ""
    for j in range(sm+1):
        st += str(dp[i][j]) + " "
    print(st)"""

print(dp[n][sm])