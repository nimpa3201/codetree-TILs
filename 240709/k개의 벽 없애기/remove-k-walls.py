from collections import deque
n,k = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(n)]
r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
visited =[[[0] * n for _ in range(n)] for _ in range(k+1)]
q = deque()

def bfs():
    dirs = { 0 : (1,0), 1 : (0,1), 2 : (-1,0) , 3 : (0,-1) }
    while q:
        x,y,step,check= q.popleft()

        if x == r2-1 and y == c2-1:
            return step

        for i in range(4):
            nx = x+ dirs[i][0]
            ny = y +dirs [i][1]

            if 0<= nx < n and 0<= ny < n and not visited[check][nx][ny]:
                if grid[nx][ny] ==0:
                    visited[check][nx][ny] =1
                    q.append((nx,ny,step+1,check))
                else:
                    if check < k :
                        q.append((nx,ny,step+1,check+1))
                        visited[check][nx][ny]=1
    return -1
        










q.append((r1-1,c1-1,0,0))
visited[0][r1-1][c1-1]=1
result =bfs()
print(result)