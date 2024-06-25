num = int(input())


def fun(k):
    if k == num+1:
        return tmp
    else:
        if k <=2:
            return k
        else:
           tmp =fun(k//3)+fun(k-1)
           return tmp

print(fun(num))