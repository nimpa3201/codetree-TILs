n,k = map(int,input().split())
arr = list(map(int,input().split()))

count = dict()
ans =0
for i in range(n):
    diff = k - arr[i]
    for j in range(i+1,n):
        diff2 = diff - arr[j]
        
        if diff2 in count:
            ans += count[diff2]

    if arr[i] not in count:
        count[arr[i]] =1
    else:
        count[arr[i]] +=1
print(ans)