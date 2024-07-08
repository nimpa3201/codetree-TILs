n = int(input())
arr = []
remove = []
for _ in range(n):
    arr.append(int(input()))

for i in range(2):
    s,e = map(int,input().split())
    remove.append((s,e))

for s,e in remove:
    temp_idx=0
    temp = [0] * n
    for i in range(s-1,e):
        arr[i] =0
    for i in range(n):
        if arr[i] !=0 :
            temp[temp_idx]= arr[i]
            temp_idx+=1
            

    arr = temp

cnt =0
for i in arr:
    if i !=0 :
        cnt+=1
print(cnt)
for i in range(cnt):
    print(arr[i])