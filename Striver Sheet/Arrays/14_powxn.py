# Pow(X,n)
# https://practice.geeksforgeeks.org/problems/power-of-numbers-1587115620/1# (Similar but power is reverse of x)
# https://leetcode.com/problems/powx-n/submissions/

# Time Complexity: O(logn), Space Complexity: O(1)

x = 2.00000
n = 10

def myPow(x, n):
    ans = 1.0
    nn = n
    
    if(nn<0):
        nn = -1*nn
    
    while(nn>0):
        if(nn%2 == 1):
            ans *= x
            nn -= 1
        else:
            x *= x
            nn /= 2
    if(n<0):
        ans = 1.0/ans
    return ans

print(myPow(x, n))