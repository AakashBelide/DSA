# Count Subarrays with Xor as K
# https://www.geeksforgeeks.org/count-number-subarrays-given-xor/
# https://www.codingninjas.com/codestudio/problems/count-subarrays-with-given-xor_1115652

# Time Complexity: O(nlogn) or O(n), Space Complexity: O(n)

arr = [4, 2, 2, 6, 4]
m = 6
n = len(arr)

def xorK(arr, m, n):
    uni = {}
    c = 0
    x = 0
    for i in range(n):
        x = x^arr[i]
        if(x == m):
            c += 1
        
        tmp = x^m
        if(tmp in uni):
            c += uni[tmp]

        if(x not in uni):
            uni[x] = 1
        else:
            uni[x] += 1
         
    return c

print(xorK(arr, m, n))