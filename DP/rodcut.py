# Rod Cutting
# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]
n = 8
sm = len(length)

dp = []

for i in range(n+1):
    a = []
    for j in range(sm+1):
        if(i==0 or j==0):
            a.append(0)
        else:
            if(length[i-1]<=j):
                a.append(max(price[i-1] + a[j-length[i-1]], dp[i-1][j]))
            else:
                a.append(dp[i-1][j])
    dp.append(a)

#print(dp)
print(dp[n][sm])