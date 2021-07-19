st = ["a", "b", "c", "?"]
st = ["?", "b", "c", "?"]
st = ["?", "b", "b", "?"]
st = ["?", "b", "?"]
st = ["a", "?", "?"]

c = 0

if(st[-1] == "?" and st[0] != "?"):
    st[-1] = st[0]
    c += 1

if(st[0] == "?" and st[-1] != "?"):
    st[0] = st[-1]
    c += 1

if(st[0] == "?" and st[-1] == "?"):
    if(len(st) == 3):
        c = 25
    else:
        if(st[1] == st[-2]):
            c = 25
        else:
            c = 24

flag = 1

for i in range(1, len(st)-1):
    if(st[i] == "?"):
        if(st[i-1] != "?" and st[i+1] != "?"):
            if(st[i-1] == st[i+1]):
                c *= 25
            else:
                c *= 24
        elif(st[i-1] == "?" and st[i+1] != "?"):
            c *= (flag-2)
            flag = 1
        elif(st[i-1] != "?" and st[i+1] == "?"):
            c *= 25
            flag = 25
        elif(st[i-1] == "?" and st[i+1] == "?"):
            c *= (flag-1)
            flag -= 1

print(st, c)
