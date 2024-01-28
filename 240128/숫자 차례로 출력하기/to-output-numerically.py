n = int(input())

def plusOne(n):
    if n ==0:
        return
    else:
        plusOne(n-1)
        print(n,end =' ')
plusOne(n)
print()
def minusOne(n):
    if n ==0:
        return
    else:
        print(n,end=" ")
        minusOne(n-1)
minusOne(n)