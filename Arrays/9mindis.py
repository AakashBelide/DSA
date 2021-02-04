# Minimise the maximum difference between heights [V.IMP]
# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1#

def getMinDiff(arr, n, k): 
    arr.sort()
    res = arr[n-1] - arr[0]
    for i in range(n-1):
        mn = min(arr[0]+k, arr[i+1]-k)
        mx = max(arr[n-1]-k, arr[i]+k)
        if(mn<0):
            continue
        res = min(res, mx - mn)
    return res

#ar = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
#print(getMinDiff(ar, 10, 5))

ar = [3, 9, 12, 16, 20]
print(getMinDiff(ar, 5, 3))

'''Reference link:
https://stackoverflow.com/questions/32233916/minimum-difference-between-heights-of-towers/63220955#63220955'''