# Evaluate Expression to True Boolean Parenthesization Recursive
# https://practice.geeksforgeeks.org/problems/boolean-parenthesization5610/1

st = "T|F&T"
s = list(st)

def solve(s, i, j, isTrue):
    if(i > j):
        return 1
    
    if(i == j):
        if(isTrue):
            return int(s[i]=="T")
        else:
            return int(s[i]=="F")

    ans = 0

    for k in range(i+1, j, 2):
        lt = solve(s, i, k-1, True)%1003
        lf = solve(s, i, k-1, False)%1003
        rt = solve(s, k+1, j, True)%1003
        rf = solve(s, k+1, j, False)%1003

        if(s[k]=="&"):
            if(isTrue==True):
                ans += lt*rt
            else:
                ans += lt*rf + lf*rt + lf*rf
        elif(s[k]=="|"):
            if(isTrue==True):
                ans += lt*rf + lf*rt + lt*rt
            else:
                ans += lf*rf
        elif(s[k]=="^"):
            if(isTrue==True):
                ans += lt*rf + lf*rt
            else:
                ans += lf*rf + lt*rt
    ans = ans%1003
    return ans

print(solve(s, 0, len(s)-1, True))