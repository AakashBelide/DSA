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
                s = arr[s]
            else:
                print(s, arr[s+1:s+arr[s]+1], s+arr[s]+1)
                if(s+arr[s]+1 >= n):
                    j += 1
                    break
                if(arr.index(max(arr[s+1:s+arr[s]+1])) == 0):
                    s += 1
                else:
                    s = arr.index(max(arr[s+1:s+arr[s]+1]))
            j += 1
    return j

ar = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

#ar = [1, 4, 3, 2, 6, 7]

#ar = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]

#ar = [1, 3, 6, 1, 0, 9]

#ar = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

n = len(ar)

print(minjump(ar, n))
