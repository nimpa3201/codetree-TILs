from collections import deque
n = int(input())
r1,c1,r2,c2 = tuple(map(int, input().split()))

visited = [
    [0]*(n+1)
    for _ in range(n+1)
]

#큐 만들기
q = deque()

# 조건 만들기
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] #and grid[x][y]

def BFS():
    while q:
        x,y,step = q.popleft()
        if x == r2 and y ==c2:
            return step

        dxs, dys = [-2,-2,-1,-1,1,1,2,2], [-1,1,-2,2,-2,2,-1,1]
        for dx, dy in zip(dxs, dys):
            new_dx = x+dx
            new_dy = y+dy
            if can_go(new_dx, new_dy):
                visited[new_dx][new_dy] = 1
                q.append((new_dx, new_dy,step+1))
    return step



q.append((r1,c1,0))
visited[r1][c1]= 1
ans =BFS()
if not visited[r2][c2]:
    print(-1)
else:
    print(ans)