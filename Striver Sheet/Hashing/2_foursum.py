# 4 Sum problem
# https://leetcode.com/problems/4sum/

# Time Complexity: O(n^3), Space Complexity: O(1)

nums = [1,0,-1,0,-2,2]
target = 0

def fourSum(nums, target):
        nums.sort()
        ans = []
        n = len(nums)
        i = 0
        while i<n:
            j = i+1
            while j<n:
                n_t = target - nums[i] - nums[j]
                left = j+1
                right = n-1
                while left<right:
                    sm = nums[left] + nums[right]
                    if(sm<n_t):
                        left += 1
                    elif(sm>n_t):
                        right -= 1
                    else:
                        #print(ans)
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while(left<right and nums[left] == ans[-1][2]):
                            left += 1
                        while(left<right and nums[right] == ans[-1][3]):
                            right -= 1
                while(j+1<n and nums[j+1] == nums[j]):
                    j += 1
                j += 1
            while(i+1<n and nums[i+1] == nums[i]):
                    i += 1
            i += 1
        return ans

print(fourSum(nums, target))