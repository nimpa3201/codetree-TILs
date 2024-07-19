from collections import deque
n,k = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(n)]
visited = [ [0] * n for _ in range(n) ]
step = [ [0] * n for _ in range(n) ]


def bfs():
    global step
    dirs = { 0 : (1,0), 1:(0,1), 2: (-1,0), 3:(0,-1)}
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+ dirs[i][0]
            ny = y +dirs[i][1]
            if 0<= nx < n and 0<= ny < n and not visited[nx][ny] and grid[nx][ny] ==1:
                visited[nx][ny]=1
                step[nx][ny] = step[x][y]+1
                q.append((nx,ny))



    

        







q =deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            q.append((i,j))
            visited[i][j]
bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] ==0:
            step[i][j] =-1
        if not visited[i][j] and grid[i][j] ==1:
            step[i][j] = -2

for i in range(n):
    for j in range(n):
        print(step[i][j],end =" ")
    print()