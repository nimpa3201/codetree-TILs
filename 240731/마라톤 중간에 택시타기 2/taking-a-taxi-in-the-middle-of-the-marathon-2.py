import sys
n = int(input())
arr= []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
min_val = sys.maxsize


for i in range(1,n-1):
    arr_j =[]
    for j in range(n):
        if i ==j:
            continue
        else:
            arr_j.append(arr[j])
    ans =0
    for k in range(len(arr_j)-1):
        ans += abs(arr_j[k][0]-arr_j[k+1][0]) + abs(arr_j[k][1]-arr_j[k+1][1])
    min_val = min(min_val,ans)
print(min_val)