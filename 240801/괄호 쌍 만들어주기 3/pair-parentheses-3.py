arr = list((input()))
cnt =0
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == "(" and arr[j] == ")":
            cnt+=1
print(cnt)