# 10 Minimum Element in Stack with Extra space
# https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
# https://leetcode.com/problems/min-stack/


s = []
ss = []

def push(s, el, ss):
    s.append(el)
    if(len(ss) == 0 or el<= ss[-1]):
        ss.append(el)

def pop(s, ss):
    if(len(s) == 0):
        return -1
    if(s[-1] == ss[-1]):
        ss.pop()
    s.pop()

def min_ele(ss):
    if(len(ss) == 0):
        return -1
    return ss[-1]