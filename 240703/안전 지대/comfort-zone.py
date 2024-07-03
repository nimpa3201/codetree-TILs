import sys
sys.setrecursionlimit(2500)

n,m = map(int,input().split())
grid =[list(map(int,input().split()))for _ in range(n)]
k = max(map(max,grid))
sf_num=1
count=0
dirs = {0 : (0,1), 1 : (1,0), 2 :(0,-1), 3:(-1,0)}
ans=0

def is_range(x,y):
    return 0<=x<n and 0<=y<m
def can_go(x,y,t):
    return is_range(x,y) and not visited[x][y] and grid[x][y] >t 
def dfs(x,y,t):
    visited[x][y] =1
    for i in range(4):
        nx = x+dirs[i][0]
        ny = y +dirs[i][1]
        if can_go(nx,ny,t):
            dfs(nx,ny,t)

for t in range(1,k+1):
    visited=[[0 for _ in range(m)] for _ in range(n)]
    count=0
    for col in range(n):
        for row in range(m):
            if can_go(col,row,t):
                visited[col][row]=True
                count+=1
                dfs(col,row,t)
    if ans <count :
        ans = count
        sf_num =t

print(sf_num,ans)