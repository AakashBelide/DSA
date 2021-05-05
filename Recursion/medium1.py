#Kth symbol in grammar (recursion)
import sys
sys.setrecursionlimit(10**6)

a = int(input("Enter first digit (N): "))
b = int(input("Enter second digit (K): "))

def kthGrammar(N, K):
    if (N == 1 and K == 1):
        return 0
    mid = (2**(N-1))/2
    if K<=mid:
        return kthGrammar(N-1,K)
    else:
        ans = kthGrammar(N-1,K-mid)
        if(ans == 0):
            return 1
        else:
            return 0

#From leetcode discussion
def kthGrammar2(N, K):
    if (N == 1):
        return 0
    else:
        if K%2:
            return kthGrammar2(N-1,(K-1)//2+1)
        else:
            return 1-kthGrammar2(N-1,(K-1)//2+1)

print(kthGrammar(a, b))
print(kthGrammar2(a, b))