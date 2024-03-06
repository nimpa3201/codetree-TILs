n,m = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(n)]
cnt1=1
cnt2=1
ans =0
result=0
for i in range(n):
    tmp = arr[i][0]
    for j in range(n-1):
        if tmp == arr[i][j+1]:
            cnt1+=1
           
        else:
            tmp = arr[i][j+1]
            ans = max(ans,cnt1)
            cnt1=1
        ans = max(ans,cnt1)
    if ans >=m :
        result+= 1 
    #print(ans)   
    cnt1 =1
    ans =0


for i in range(n):
    tmp = arr[0][i]
    for j in range(n-1):
        if tmp == arr[j+1][i]:
            cnt2+=1
        else:
            tmp = arr[j+1][i]
            ans = max(ans,cnt2)
            cnt2=1
        ans = max(ans,cnt2)
    if ans >=m :
        result+= 1
    #print(ans)    
    cnt2 =1
    ans=0
print(result)