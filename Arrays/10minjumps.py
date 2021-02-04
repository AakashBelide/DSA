# Minimum no. of Jumps to reach end of an array
# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

def minjump(arr, n):
    j = 0
    s = 0
    while(s<n):
        if(arr[s] == 0):
            break
        else:
            if(s == 0):
                s += arr[s]
            else:
                #print(s, arr[s:s+arr[s]])
                s += max(arr[s:s+arr[s]])
            j += 1
    return j

ar = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = 11

#ar = [1, 4, 3, 2, 6, 7]
#n = 6

print(minjump(ar, n))
