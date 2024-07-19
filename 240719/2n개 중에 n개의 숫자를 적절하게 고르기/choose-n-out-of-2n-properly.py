n = int(input())
arr = list(map(int,input().split()))
ans =sum(arr)+1
tmp =0
k=0
result =0
def comb(s,cnt,acc):
    global ans,result,k,tmp
    if cnt ==n:
        tmp = sum(arr) - acc
        result =tmp -acc
    for i in range(s,2*n):
        acc+=arr[i]
       
        comb(i+1,cnt+1,acc)
        acc-=arr[i]
    ans= min(ans,abs(result))

comb(0,0,0)
print(ans)