n = int(input())

def func(k):
    if k ==0:
        return
    else:
        print(k,end=' ')
        func(k-1)
        print(k,end=' ')
func(n)