# Grid Unique Paths
# https://practice.geeksforgeeks.org/problems/count-all-possible-paths-from-top-left-to-bottom-right3011/1#
# https://leetcode.com/problems/unique-paths/

# Time Complexity: O(m-1), Space Complexity: O(1)

m = 3
n = 7

def uniquePaths(m, n):
    import math
    if not m or not n:
        return 0
    return int(math.factorial(m+n-2)/(math.factorial(n-1) * math.factorial(m-1)))

print(uniquePaths(m, n))

def numberOfPaths( m, n):
    ans = 1
    for i in range(n, (m + n - 1)):
        ans *= i
        ans //= (i - n + 1)
    return int(ans%(10**9 + 7))

print(numberOfPaths(m, n))