n = int(input())
arr= [list(map(int,input().split())) for _ in range(n)]


max_val =0

for i in range(n):
    for j in range(n-2):
        max_val = max(max_val,arr[i][j]+arr[i][j+1]+arr[i][j+2])
print(max_val)