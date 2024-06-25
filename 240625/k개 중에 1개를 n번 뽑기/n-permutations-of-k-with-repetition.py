k,n = map(int,input().split()) #k이하의 숫자  N번 뽑음
ans =[]

def fun(cnt,n):
    if cnt == n:
        print(*ans)

    else:
        for i in range(1,k+1):
            ans.append(i)
            fun(cnt+1,n)
            ans.pop()

fun(0,n)