# Scrambled String Recursive
# https://www.geeksforgeeks.org/check-if-a-string-is-a-scrambled-form-of-another-string/
# https://leetcode.com/problems/scramble-string/

s1 = "great"
s2 = "eatgr"

def solve(a, b):
    if(a == b):
        return True
    
    if(len(a)<=1):
        return False
    
    n = len(a)
    flag = False

    for i in range(1, n):
        print(i)
        print("a[:i]: " + a[:i] + " ,b[n-i:]: " + b[n-i:] + " ,a[i:]: " + a[i:] + " ,b[:n-i]: " + b[:n-i])
        print("a[:i]: " + a[:i] + " ,b[:i]: " + b[:i] + " ,a[i:]: " + a[i:] + " ,b[i:]: " + b[i:])
        cond1 = solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i])
        cond2 = solve(a[:i], b[:i]) and solve(a[i:], b[i:])
        
        if(cond1 or cond2):
            flag = True
            break
    
    return flag

print(solve(s1, s2))