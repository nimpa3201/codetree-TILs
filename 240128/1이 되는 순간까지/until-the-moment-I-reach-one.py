def fun(n):
    global cnt
    if n ==1:
        return cnt

    else:
        if n %2==0:
            cnt+=1
            fun(n//2)
            
        else:
            cnt+=1
            fun(n//3)
           
N = int(input())
cnt=0
fun(N)
print(cnt)