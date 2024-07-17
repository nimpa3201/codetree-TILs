from collections import deque
n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dots = []
q = deque()

for _ in range(k):
    r, c = map(int, input().split())
    q.append((r - 1, c - 1))
    visited[r - 1][c - 1] = 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            dots.append((i, j))

def bfs(start_p):
    dirs = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque(start_p)
    for x, y in start_p:
        visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx= x + dirs[i][0]
            ny = y + dirs[i][1]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1 
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                cnt += 1
    return cnt

ans = 0
def combinations(start, comb):
    global ans
    if len(comb) == m:
        for x, y in comb:
            grid[x][y] = 0
        reach = bfs(q)
        ans = max(ans, reach)
        for x, y in comb:
            grid[x][y] = 1
        return

    for i in range(start, len(dots)):
        comb.append(dots[i])
        combinations(i + 1, comb)
        comb.pop()

combinations(0, [])

print(ans)