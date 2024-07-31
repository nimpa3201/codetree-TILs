n = int(input())
graph = [list(map(int,input().split()))for _ in range(n)]



for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] ==1 or graph[i][k]+graph[k][j]==2 or i ==j:
                graph[i][j] =1

for i in range(n):
    for j in range(n):
        print(graph[i][j],end=" ")
    print()