n = int(input())
arr =[]
for _ in range(n):
    arr.append(int(input()))

if n ==1:
    print(1)
    exit()

ans =0
cnt=1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        cnt+=1
        ans = max(ans,cnt)
    else:
        ans = max(ans,cnt)
        cnt =1
print(ans)