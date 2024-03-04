n = int(input())
arr = [list(map(int,input().split()))for _ in range(n)]
ans =0
for row in range(n):
    for col in range(n):
        matrix=0
        if row+3 > n or col+3> n :
            continue
        for i in range(row,row+3):
            for j in range(col,col+3):
                matrix += arr[i][j]
        ans = max(ans,matrix)
print(ans)