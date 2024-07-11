n = int(input()) # 노드개수
edges = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
parent = [0] * (n+1)
for _ in range(n-1):
    e1,e2 = map(int,input().split())
    edges[e1].append(e2)
    edges[e2].append(e1)



def traversal(n):
    for node in edges[n]:
        if not visited[node]:
            visited[node]=1
            parent[node] = n
            traversal(node)


visited[1] =1
traversal(1)
for p in parent[2:]:
    print(p)