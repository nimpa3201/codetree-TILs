num = int(input())

def fun(k):
    if k == num+1:
        return temp
    else:
        if k ==1:
            return 2
        if k ==2: 
            return 4
        else:
            temp = fun(k-2)*fun(k-1) % 100 
            return temp 

print(fun(num))