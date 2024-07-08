n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
arr = [[0 for _ in range(n)] for _ in range(n)]  
r,c = map(int,input().split())
tmp = grid[r-1][c-1]
dirs={0:(-1,0),1:(1,0),2:(0,1),3:(0,-1)}
def power(cnt,row,col,d,board):
    if cnt == tmp-1:
        return 
    if 0<=row < n and 0<= col<n:   
        grid[row][col]=0
        power(cnt+1,row+dirs[d][0],col+dirs[d][1],d,board)

def run(x,y,board):
    grid[x][y] =0
    power(0,x+dirs[0][0],y+dirs[0][1],0,board)
    power(0,x+dirs[1][0],y+dirs[1][1],1,board)
    power(0,x+dirs[2][0],y+dirs[2][1],2,board)
    power(0,x+dirs[3][0],y+dirs[3][1],3,board)
    return grid

bomb = run(r-1,c-1,grid)

for row in range(n):
    arr_index = n-1
    for col  in range(n-1,-1,-1):
        if bomb[col][row] !=0:
            arr[arr_index][row] = bomb[col][row]
            arr_index-=1


for i in arr:
    print(*i)