import re

s = "BANANA"
vowels = "AEIUO"
a = "Stuart"
st = []
a1 = 0
b = "Kevin"
kv = []
b1 = 0
x = []
sop = ""

def solve(a, b):
    if (len(a) == 0):
        x.append(b)
        return
    else:
        b1 = b
        b2 = b
        b2 = b2 + a[0]
        a = a[1:]
        solve(a, b1)
        solve(a, b2)
        return

solve(s, sop)

def CountOccurrences(string, substring): 
  
    # Initialize count and start to 0 
    count = 0
    start = 0
  
    # Search through the string till 
    # we reach the end of it 
    while start < len(string): 
  
        # Check if a substring is present from 
        # 'start' position till the end 
        pos = string.find(substring, start) 
  
        if pos != -1: 
            # If a substring is present, move 'start' to 
            # the next position from start of the substring 
            start = pos + 1
  
            # Increment the count 
            count += 1
        else: 
            # If no further substring is present 
            break
    # return the value of count 
    return count

for i in range(len(x)):
    if(x[i]!="" and x[i] not in st and x[i][0] not in vowels):
        st.append(x[i])
    elif(x[i]!="" and x[i] not in kv and x[i][0] in vowels):
        kv.append(x[i])
    
for j in st:
    ssc = CountOccurrences(s, j)
    a1 += ssc
    
for k in kv:
    ksc = CountOccurrences(s,k)
    b1 += ksc
if(a1>b1):
    print(a + " " + str(a1))
elif(a1<b1):
    print(b + " " + str(b1))
elif(a1==b1):
    print("Draw")