# 0-1 Knapsack Recursive

def knapsack(wt, val, w, n):
    if(n == 0 or w == 0):
        return 0
    
    if(wt[n-1]<=w):
        return max(val[n-1] + knapsack(wt, val, w-wt[n-1], n-1), knapsack(wt, val, w, n-1))
    else:
        return knapsack(wt, val, w, n-1)
wt = [1,3,4,5]
val = [1,4,5,7]
w = 7
n = len(wt)

print(knapsack(wt, val, w, n))