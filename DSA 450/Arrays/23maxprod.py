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

# GFG Solution - Time Complexity: O(N)
def maxsubarrayproduct(arr, n):
    max_ending_here = 1
    min_ending_here = 1
    max_so_far = 0
    flag = 0
    
    for i in range(0, n):
        if arr[i] > 0:
            max_ending_here = max_ending_here * arr[i]
            min_ending_here = min (min_ending_here * arr[i], 1)
            flag = 1
        
        elif arr[i] == 0:
            max_ending_here = 1
            min_ending_here = 1
        
        else:
            temp = max_ending_here
            max_ending_here = max (min_ending_here * arr[i], 1)
            min_ending_here = temp * arr[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
             
    if flag == 0 and max_so_far == 0:
        return 0
    return max_so_far

#Leetcode discussion solution - Time Complexity: O(N)
def maxProduct2(nums, n):
    curr_max = global_max = curr_min = nums[0]
    
    for i in range(1,n):
        #print("First", global_max, curr_max, curr_min)
        #print("Second", nums[i], nums[i] * curr_max, nums[i] * curr_min)
        curr_max, curr_min = max(nums[i], nums[i] * curr_max, nums[i] * curr_min), min(nums[i], nums[i] * curr_max, nums[i] * curr_min)
        #print("Third", global_max, curr_max, curr_min)
        global_max = max(global_max, curr_max)


    return global_max

arr = [6, -3, -10, 0, 2]
n = 5

print(maxProduct(arr, n))
print(maxsubarrayproduct(arr, n))
print(maxProduct2(arr, n))