n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dirs = {0 :(0, -1), 1 : (-1, 0), 2: (1, 0), 3: (0, 1)}

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y]

def dfs(x, y, value):
    visited[x][y] = 1
    count = 1
    
    for i in dirs:
        nx, ny = x + dirs[i][0], y + dirs[i][1]
        if can_go(nx, ny) and graph[nx][ny] == value:
            count += dfs(nx, ny, value)
    
    return count


totalBlock = 0
maxSize = 0

for col in range(n):
    for row in range(n):
        if not visited[col][row]:
            result = dfs(col, row, graph[col][row])
            if result >= 4:
                totalBlock += 1
            maxSize = max(maxSize,result)

print(totalBlock, maxSize)