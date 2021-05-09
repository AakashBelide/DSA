# Equal Sum Partition
# https://leetcode.com/problems/partition-equal-subset-sum/

arr = [1, 5, 11, 5]

def canPartition(nums):
    if(sum(nums)%2!=0):
        return False
    n = len(nums)
    sm = sum(nums)//2
    dp = []
    for i in range(n+1):
        a = []
        for j in range(sm+1):
            if(i==0 and j==0):
                a.append(True)
            if(i==0):
                a.append(False)
            elif(j==0):
                a.append(True)
            else:
                if(nums[i-1]<=j):
                    a.append(dp[i-1][j-nums[i-1]] or dp[i-1][j])
                else:
                    a.append(dp[i-1][j])
        dp.append(a)
    return dp[n][sm]

print(canPartition(arr))