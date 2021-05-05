# Minimum no. of Jumps to reach end of an array
# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1


# Editorial Solution - Time Complexity: O(n)
def minjump(arr, n):
    if(n<=1):
        return 0
    
    if(arr[0] == 0):
        return -1
    
    maxReach = arr[0]
    step = arr[0]
    jump = 1
    for i in range(1, n):
        if(i == n-1):
            return jump
        
        maxReach = max(maxReach, i+arr[i])
        
        step -= 1
        
        if(step == 0):
            jump += 1
        
            if(i>=maxReach):
                return -1
            
            step = maxReach - i
    return -1

ar = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

#ar = [1, 4, 3, 2, 6, 7]

#ar = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]

#ar = [1, 3, 6, 1, 0, 9]

#ar = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

n = len(ar)

print(minjump(ar, n))
