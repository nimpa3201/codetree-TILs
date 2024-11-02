n = int(input())
tree = [[] for _ in range(n+1)]
visited = [ 0 for _ in range(n+1)]
for _ in range(n-1):
    a,b,w = map(int,input().split())
    tree[a].append((b,w))
    tree[b].append((a,w))


ans =0
idx =0
def dfs(parent,acc):
    global ans, idx
    for child ,weight in tree[parent]:
        if not visited[child]:
            visited[child]=1
            dfs(child,acc+weight)
            visited[child] =0
    
    if ans < acc:
        ans =acc
        idx = parent
    return idx ,ans


visited[1] =1
start,ans = dfs(1,0)
visited = [ 0 for _ in range(n+1)]
visited[start]=1
end = dfs(start,0)
print(end[1])