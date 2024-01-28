def oneToN(n):
    if n ==1:
        return 1
    else :
        return oneToN(n-1) + n

N = int(input())

print(oneToN(N))