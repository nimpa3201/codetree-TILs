n = int(input())
visited = [0 for _ in range(n+1)]
ans =[]

def pem(k):
    global ans
    if k == n:
        print(*ans)
        return
    for i in range(1,n+1):
        if not visited[i]:
            ans.append(i)
            visited[i] =1
            pem(k+1)
            ans.pop()
            visited[i]=0

pem(0)