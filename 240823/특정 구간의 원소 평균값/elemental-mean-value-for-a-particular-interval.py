N = int(input())
arr = list(map(int,input().split()))
cnt =0
for i in range(N):
    for j in range(i+1,N+1):
        sum_val =0
        tmp =[]
        for k in range(i,j):
            sum_val+=arr[k]
            tmp.append(arr[k])
        ans =sum_val/(j-i)
        if ans in tmp:
            cnt+=1

print(cnt)