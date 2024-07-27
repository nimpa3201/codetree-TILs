OFFSET = 100

n = int(input())
arr =[0 for _ in range(201)]
for _ in range(n):
    s,e = map(int,input().split())
    for i in range(OFFSET+s,OFFSET+e):
        arr[i]+=1
print(max(arr))