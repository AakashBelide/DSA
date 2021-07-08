# Evaluate Expression to True Boolean Parenthesization Recursive
# https://practice.geeksforgeeks.org/problems/boolean-parenthesization5610/1
# https://www.interviewbit.com/problems/evaluate-expression-to-true/

st = "T^F|F"
s = list(st)

dp = {}

def solve(s, i, j, isTrue):
    if(i > j):
        return 1
    
    if(i == j):
        if(isTrue):
            return int(s[i]=="T")
        else:
            return int(s[i]=="F")
    
    st_tmp = str(i) + " " + str(j) + " " + str(int(isTrue))
    if st_tmp in dp:
        return dp[st_tmp]

    ans = 0

    for k in range(i+1, j, 2):
        lt_st_tmp = str(i) + " " + str(k-1) + " " + str(True)
        lf_st_tmp = str(i) + " " + str(k-1) + " " + str(False)
        rt_st_tmp = str(k+1) + " " + str(j) + " " + str(True)
        rf_st_tmp = str(k+1) + " " + str(j) + " " + str(False)

        if lt_st_tmp in dp:
            lt = dp[lt_st_tmp]
        else:
            lt = solve(s, i, k-1, True)%1003
        
        if lf_st_tmp in dp:
            lf = dp[lf_st_tmp]
        else:
            lf = solve(s, i, k-1, False)%1003
        
        if rt_st_tmp in dp:
            rt = dp[rt_st_tmp]
        else:
            rt = solve(s, k+1, j, True)%1003
        
        if rf_st_tmp in dp:
            rf = dp[rf_st_tmp]
        else:
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
    dp[st_tmp] = ans%1003
    return ans

print(solve(s, 0, len(s)-1, True))