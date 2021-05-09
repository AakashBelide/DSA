# Count of Subset Sum
# https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/

arr = [2, 3, 5, 6, 8, 10]
sm = 10
n = len(arr)

dp = []
for i in range(n+1):
    a = []
    for j in range(sm+1):
        if(i==0 and j==0):
            a.append(1)
        elif(i==0):
            a.append(0)
        elif(j==0):
            a.append(1)
        else:
            if(arr[i-1]<=j):
                a.append(dp[i-1][j-arr[i-1]] + dp[i-1][j])
            else:
                a.append(dp[i-1][j])
    dp.append(a)

print(dp[n][sm])