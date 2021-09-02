# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1

# Time Complexity: O(n), Space Complexity: O(n)

st = "abcaabcdba"

def lswrc(s):
    l = 0
    r = 0
    n = len(s)
    mx = 0
    uni = {}
    while r<n:
        if(s[r] in uni):
            if(uni[s[r]]>=l):
                l = uni[s[r]] + 1
        uni[s[r]] = r
        r += 1
        mx = max(mx, r-l)
    return mx

print(lswrc(st))