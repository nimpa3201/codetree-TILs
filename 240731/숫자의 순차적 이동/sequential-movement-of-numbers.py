n,m = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(n)]
cnt =1
dirs = {0 :(-1,0), 1:(-1,1), 2:(0,1), 3:(1,1), 4:(1,0), 5:(1,-1), 6:(0,-1), 7:(-1,-1)}
max_val =0
tmp =0

def change():
    for num in range(1,(n*n)+1) :
        for i in range(n):
            for j in range(n):
                if arr[i][j] ==num :
                    x,y = i,j
                    tmp = arr[i][j]
                    max_val =0
                    for dir_num in range(8):
                        nx = x + dirs[dir_num][0]
                        ny = y + dirs[dir_num][1]
                        if 0<= nx < n and 0<=ny < n:
                            if max_val < arr[nx][ny]:
                                max_val = arr[nx][ny]
                                pos_x = nx
                                pos_y = ny
        arr[x][y] = max_val
        arr[pos_x][pos_y] =tmp

for _ in range(m):
    change()

for row in arr:
    print(*row)