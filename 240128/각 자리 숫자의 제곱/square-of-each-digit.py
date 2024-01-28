def squreNum(k):
    if k < 10:
        return k**2
    else:
        return squreNum(k//10)+(k%10)**2    
n = int(input())
print(squreNum(n))