#sorting an array using recursion only

v = [int(i) for i in input("Enter the list/array elements with spaces between each of them: ").split()]


def insrt(a, b):
    if (len(a) == 0 or a[-1]<=b):
        a.append(b)
        return
    c = a.pop()
    insrt(a, b)
    a.append(c)
    return a

def srt(x):
    if (len(x) == 1):
        return
    y = x.pop()
    srt(x)
    insrt(x, y)
    return x

print(srt(v))