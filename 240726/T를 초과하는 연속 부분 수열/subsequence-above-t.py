n,t = map(int,input().split())
arr =list(map(int,input().split()))
if n ==1:
    if n > t:
        print(1)
    else:
        print(0)

else:
    ans =0
    cnt =1
    for i in range(n-1):
        if arr[i] > t and arr[i+1] >t:
            cnt+=1
        else:
            cnt =1
        ans = max(ans,cnt)

print(ans)