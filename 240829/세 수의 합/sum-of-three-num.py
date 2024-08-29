n,k = map(int,input().split())
arr = list(map(int,input().split()))
cnt =0

def fun(num,tmp,start):
    global cnt
    if num == 3:
        if sum(tmp) == k:
            cnt+=1
        return

    for i in range(start,n):
        tmp.append(arr[i])
        fun(num+1,tmp,i+1)
        tmp.pop()

fun(0,[],0)
print(cnt)