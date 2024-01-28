def fun(n):
    if n<=2:
        return n
    else:
        if n%2==0:
            return n+fun(n-2)
        else:
            return n+fun(n-2)

N = int(input())
print(fun(N))