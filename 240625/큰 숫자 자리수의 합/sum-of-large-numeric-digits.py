a,b,c = map(int,input().split())
tmp = a*b*c

def fun(tmp):
    if tmp <=9:
        return tmp
    else:
        return fun(tmp//10)+tmp%10

print(fun(tmp))