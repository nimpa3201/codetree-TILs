def fibo(n):
    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-1)

N = int(input())
print(fibo(N))