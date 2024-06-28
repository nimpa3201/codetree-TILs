n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
ans = n * 10000 + 1

def circle(arr, graph):
    global ans
    tmp = 0
    for i in range(n - 1):
        if graph[arr[i]][arr[i + 1]] == 0:
            return -1
        tmp += graph[arr[i]][arr[i + 1]]
    if graph[arr[-1]][arr[0]] == 0:
        return -1
    tmp += graph[arr[-1]][arr[0]]
    ans = min(ans, tmp)
    return ans

def perm(k, arr, n):
    global ans
    if k == n:
        circle(arr, graph)
        return
    for i in range(n):
        if not visited[i]:
            arr.append(i)
            visited[i] = 1
            perm(k + 1, arr, n)
            arr.pop()
            visited[i] = 0

perm(0, [], n)
print(ans)