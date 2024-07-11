n = int(input())
edges = [[] for _ in range(n+1) ]
visited = [0 for _ in range(n+1)]
for _ in range(n-1):
    e1,e2,w = map(int,input().split())
    edges[e1].append((e2,w))
    edges[e2].append((e1,w))


ans =0
idx =0
def dfs(curr,acc,visited,edges):
    global ans,idx
    for node in edges[curr]:
        if not visited[node[0]]:
            visited[node[0]]=1
            dfs(node[0],acc+node[1],visited,edges)
            visited[node[0]]=0
    
    if ans < acc :
        ans =acc
        idx = curr
    return idx, ans
start = dfs(1,0,visited,edges)
visited[1] =1
visited = [0 for _ in range(n+1)]
ans =0
visited[start[0]] =1
end=dfs(start[0],0,visited,edges)
print(end[1])