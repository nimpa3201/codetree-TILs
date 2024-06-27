n = int(input())
ans =[]
visited = [0 for _ in range(n+1)]
def reverPerm(k):
    if k ==n:
        print(*ans)
        return
    
    for i in range(n,0,-1):
        if not visited[i]:
            ans.append(i)
            visited[i] =1
            reverPerm(k+1)
            ans.pop()
            visited[i] =0

reverPerm(0)