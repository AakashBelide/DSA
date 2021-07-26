# Reverse Pairs (Leetcode)
# https://leetcode.com/problems/reverse-pairs/

# Time Complexity: O(nlogn), Space Complexity: O(n)

arr = [1,3,2,3,1]

def reversePairs(nums):
    def merge(nums, low, mid, high):
        ct = 0
        j = mid+1
        for i in range(low, mid+1):
            while(j<=high and nums[i]>(2*nums[j])):
                j += 1
            
            ct += (j - (mid + 1))
        
        tmp = []
        left = low
        right = mid+1
        
        while(left<=mid and right<=high):
            if(nums[left]<=nums[right]):
                tmp.append(nums[left])
                left += 1
            else:
                tmp.append(nums[right])
                right += 1
        
        while(left<=mid):
            tmp.append(nums[left])
            left += 1
        
        while(right<=high):
            tmp.append(nums[right])
            right += 1
        
        for i in range(low, high+1):
            nums[i] = tmp[i-low]
        
        return ct
        
        
    
    def mergeSort(nums, low, high):
        if(low>=high):
            return 0
        mid = (low + high)//2
        c = 0
        c += mergeSort(nums, low, mid)
        c += mergeSort(nums, mid+1, high)
        c += merge(nums, low, mid, high)
        
        return c
    
    return mergeSort(nums, 0, len(nums)-1)

print(reversePairs(arr))