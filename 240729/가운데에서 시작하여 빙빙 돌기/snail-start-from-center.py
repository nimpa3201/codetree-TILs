n =int(input())
squre= [[0]*n for _ in range(n)]
x,y =n-1,n-1
squre[x][y] = n*n


dirs = { 0: (0,-1), 1:(-1,0), 2:(0,1),3:(1,0) }

dir_num = 0


def is_range(x,y):
    return 0<=x<n and 0<=y<n
        


for i in range(n * n-1,0,-1):

    nx, ny = x + dirs[dir_num][0], y + dirs[dir_num][1]
    

    if not is_range(nx, ny) or squre[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x, y =  x + dirs[dir_num][0], y + dirs[dir_num][1]
    squre[x][y] = i

    


for num in squre:
    print(*num)