from collections import deque

n, h, m = tuple(map(int, input().split()))
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dot = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if graph[i][j] == 3
]

q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
distances = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and graph[x][y] != 1 and not visited[x][y]

def push(nx, ny, new_dist):
    q.append((nx, ny))
    visited[nx][ny] = True
    distances[nx][ny] = new_dist

def bfs():
    while q:
        x, y = q.popleft()
        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, distances[x][y] + 1)

for x, y in dot:
    push(x, y, 0)

bfs()

for i in range(n):
    for j in range(n):
        if graph[i][j] != 2:
            print(0, end=" ")
        else:
            if not visited[i][j]:
                print(-1, end=" ")
            else:
                print(distances[i][j], end=" ")
    print()