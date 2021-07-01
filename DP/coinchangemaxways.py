# Coin Change Maximum Ways
# https://www.geeksforgeeks.org/coin-change-dp-7/
# https://leetcode.com/problems/coin-change-2/

coins = [1,2,3]
n = len(coins)
sm = 5

dp = []

for i in range(n+1):
    a = []
    for j in range(sm+1):
        if(j==0):
            a.append(1)
        elif(i==0):
            a.append(0)
        else:
            if(coins[i-1]<=j):
                a.append(a[j-coins[i-1]] + dp[i-1][j])
            else:
                a.append(dp[i-1][j])
    dp.append(a)

#print(dp)
print(dp[n][sm])