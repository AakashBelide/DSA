# find maximum product subarray
# https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1

# Own solution - Time Complexity: O(N^2)
def maxProduct(arr, n):
    res = 1
    
    for i in range(n):
        prod = 1
        prod *= arr[i]
        if(prod==0):
            prod = 1
        if(prod > res):
            res = prod
        for j in range(i+1, n):
            prod *= arr[j]
            if(prod==0):
                prod = 1
            if(prod > res):
                res = prod
    return res

arr = [6, -3, -10, 0, 2]
n = 5

print(maxProduct(arr, n))