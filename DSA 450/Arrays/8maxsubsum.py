# find Largest sum contiguous Subarray [V. IMP]
# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

# Kadane's Algorithm Time Complexity: O(n)
# Algorithmic Paradigm: Dynamic Programming

def maxSubArraySum(a,size):
    msf = 0
    mtn = 0
    for i in range(size):
        mtn += a[i]
        if(msf<mtn):
            msf = mtn
        if(mtn<0):
            mtn = 0
    if(msf == 0):
        msf = max(a)
    return msf

#ar = [1,2,3,-2,5]

ar = [-2, -3, -3]

print(maxSubArraySum(ar, len(ar)))