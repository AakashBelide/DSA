# Maximum profit by buying and selling a share atmost twice
# https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/

# GFG using DP -  Time Complexit: O(N)
def maxProfit(price, n):
    profit = [0]*n
    
    max_price = price[n-1]
 
    for i in range(n-2, 0, -1):
        if price[i] > max_price:
            max_price = price[i]
        
        profit[i] = max(profit[i+1], max_price - price[i])
        #print(profit, max_price, price[i])
    
    min_price = price[0]
    #print("Min")
    for i in range(1, n):
        if price[i] < min_price:
            min_price = price[i]
        
        profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
        #print(profit, min_price, price[i])
 
    result = profit[n-1]
 
    return result

arr = [2, 30, 15, 10, 8, 25, 80]
n = 7

arr = [10, 22, 5, 75, 65, 80]
n = 6

arr = [100, 30, 15, 10, 8, 25, 80]
n = 7

print(maxProfit(arr, n))