# find common elements In 3 sorted arrays
# https://practice.geeksforgeeks.org/problems/common-elements1132/1

# Own solution
def commonElements(A, B, C, n1, n2, n3):
    cm = list(set(A).intersection(set(B), set(C)))
    cm.sort()
    return cm

# GFG Solution - Time Complexit: O(n1 + n2 + n3)
def commonElements2(A, B, C, n1, n2, n3):
    cm = []
    i, j, k = 0, 0, 0
    while (i < n1 and j < n2 and k< n3):
        if (A[i] == B[j] and B[j] == C[k]):
            if(A[i] not in cm):
                cm.append(A[i])
            i += 1
            j += 1
            k += 1
        
        elif A[i] < B[j]:
            i += 1
        
        elif B[j] < C[k]:
            j += 1
        
        else:
            k += 1
    return cm

n1 = 6
A = [1, 5, 10, 20, 40, 80]
n2 = 5
B = [6, 7, 20, 80, 100]
n3 = 8
C = [3, 4, 15, 20, 30, 70, 80, 120]

print(commonElements(A, B, C, n1, n2, n3))
print(commonElements2(A, B, C, n1, n2, n3))