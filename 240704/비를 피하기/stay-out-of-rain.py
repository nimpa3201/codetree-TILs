from collections import deque
n,h,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)]for _ in range(n)]
result =[[0 for _ in range(n)]for _ in range(n)]
q =deque()
dirs = {0 : (0,1), 1: (-1,0), 2: (1,0), 3:(0,-1)}
def bfs():
    global step
    ans =[]
    while q: 
        x,y,step = q.popleft()
        if graph[x][y] == 3:
            return step
            
        for i in range(4):
            nx = x+dirs[i][0]
            ny = y+dirs[i][1]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny]!=1 and graph[nx][ny]!=2:
                visited[nx][ny]= 1
                q.append((nx,ny,step+1))
               
    return -1

    

dot = []              
for i in range(n):
    for j in range(n):
        if graph[i][j] ==2:
            dot.append((i,j))

for x,y in dot:
    visited = [[0 for _ in range(n)]for _ in range(n)]
    q.append((x,y,0))
    visited[x][y]=1
    graph[x][y] =0
    
    result[x][y] = bfs()
    bfs()
    
for arr in result:
    print(*arr)