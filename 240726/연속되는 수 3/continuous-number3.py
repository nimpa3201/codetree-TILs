n = int(input())
arr =[]
for _ in range(n):
    arr.append(int(input()))
ans,cnt= 0,1

if n ==1:
    print(1)
    exit()

for i in range(n-1):
    if arr[i]*arr[i+1]> 0:
        cnt+=1
    else:
        cnt =1
    ans = max(ans,cnt)
print(ans)