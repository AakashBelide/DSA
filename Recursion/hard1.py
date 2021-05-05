#Print N-bit binary numbers having more 1’s than 0’s for any prefix

n = int(input("Enter number: "))

o = 0
c = 0
op = ""
a = []

#Own logic
def sol(v, w, x , y, z):
    if (v == 0):
        z.append(y)
        return
    
    if (w > x):
        y1 = y + "0"
        y2 = y + "1"
        sol(v-1,w,x+1,y1,z)
        sol(v-1,w+1,x,y2,z)
    
    if (w == x):
        y += "1"
        sol(v-1,w+1,x,y,z)
       
    return

#Tutorial logic
def sol_l(v, w, x , y, z):
    if (v == 0):
        z.append(y)
        return
    
    y1 = y + "1"
    sol(v-1,w+1,x,y1,z)

    if (w > x):
        y2 = y + "0"
        sol(v-1,w,x+1,y2,z) 
    return

sol_l(n, o, c, op, a)
print(a)