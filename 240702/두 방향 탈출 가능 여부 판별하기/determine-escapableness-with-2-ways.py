n,m = map(int,input().split())
graph = [list(map(int,input().split()))for _ in range(n)]
dirs = {0 : (0,1) , 1 : (1,0) } #오른쪽, 아래 
visited = [[0] * m for _ in range(n)]


def dfs(x,y):
    for i in range(len(dirs)):
        nx = x+dirs[i][0]
        ny = y +dirs[i][1]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]and graph[nx][ny]==1:
            dfs(nx,ny)
            visited[nx][ny] =1


dfs(0,0)
visited[0][0] =1
print(visited[n-1][m-1])