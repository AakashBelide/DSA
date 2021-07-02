# Matrix Chain Multiplication Recursive
# https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

arr = [40, 20, 30, 10, 30]

def solve(arr, i, j):
    if(i>=j):
        return 0

    mn = 999999999

    for k in range(i, j):
        temp = solve(arr, i, k) + solve(arr, k+1, j) + (arr[i-1] * arr[k] * arr[j])

        mn = min(temp, mn)
    
    return mn

print(solve(arr, 1, len(arr)-1))