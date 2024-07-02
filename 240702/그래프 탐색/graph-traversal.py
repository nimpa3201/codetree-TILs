n,m = map(int,input().split())
arr=[[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
visited = [0 for _ in range(n+2) ]
cnt =0
def dfs(n,visited):
    global cnt
    for i in arr[n]:
        if not visited[i]:
            cnt+=1
            visited[i] =1
            dfs(i,visited)






dfs(1,visited)
visited[1]=1
print(cnt-1)