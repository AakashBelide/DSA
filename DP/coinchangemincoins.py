# Coin Change Minimum Coins
# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
# https://leetcode.com/problems/coin-change/

import sys
coins = [1,2,3]
n = len(coins)
sm = 5

dp = []

for i in range(n+1):
    a = []
    for j in range(sm+1):
        if(i==0):
            a.append(sys.maxsize - 1)
        elif(j==0):
            a.append(0)
        elif(i==1):
            if(j%coins[0]==0):
                a.append(j//coins[0])
            else:
                a.append(sys.maxsize-1)
        else:
            if(coins[i-1]<=j):
                a.append(min(1 + a[j-coins[i-1]], dp[i-1][j]))
            else:
                a.append(dp[i-1][j])
    dp.append(a)

print(dp[n][sm])