import sys
INF = sys.maxsize
n,m = map(int,input().split())
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    r,c,d = map(int,input().split())
    dist[r][c] = d

for i in range(1,n+1):
    dist[i][i] =0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

ans = INF
for i in range(1,n+1):
    distance =0
    for j in range(1,n+1):
        if dist[i][j] != INF and dist[j][i] !=INF :
            distance +=dist[i][j]+dist[j][i]
    if distance !=0:
        ans = min(ans,distance)
print(ans)