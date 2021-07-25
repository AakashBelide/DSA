# Stock Buy and Sell
# https://practice.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1 (Similar but total profit)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Time Complexity: O(n), Space Complexity: O(1)

arr = [7,1,5,3,6,4]

def maxProfit(prices):
    if len(prices)==0:
        return 0
    profit = 0
    cost = 0
    mn = prices[0]
    for i in range(len(prices)):
        mn = min(mn, prices[i])
        cost = prices[i] - mn
        profit = max(profit, cost)
    return profit

print(maxProfit(arr))