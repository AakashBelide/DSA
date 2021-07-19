# 11 Minimum Element in Stack in O(1) Space
# https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
# https://leetcode.com/problems/min-stack/

s = []
min_ele = -1

def push(s, el, min_ele):
    if(len(s) == 0):
        s.append(el)
        min_ele = el
    else:
        if(el >= min_ele):
            s.append(el)
        else:
            s.append(2*el - min_ele)
            min_ele = el

def pop(s, min_ele):
    if(len(s) == 0):
        return -1
    if(s[-1] < min_ele):
        min_ele = 2*min_ele - s[-1]
    s.pop()

def top(s, min_ele):
    if(len(s) == 0):
        return -1
    if(s[-1] < min_ele):
        return min_ele
    else:
        return s[-1]

def min_el(min_ele):
    return min_ele