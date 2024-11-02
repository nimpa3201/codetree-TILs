# n,m = map(int,input().split())
# tree = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a,b,w = map(int,input().split())
#     tree[a].append((b,w))
#     tree[b].append((a,w))



# def dfs(node,goal,acc):
#     if node == goal:
#         return acc

#     for child,weight in tree[node]:
#         if not visited[child] :
#             visited[child]=1
#             dfs(child,goal,acc+weight)



# for _ in range(m):
#     start,end = map(int,input().split())
#     visited = [0 for _ in range(n+1)]
#     visited[start] =1
#     ans = dfs(start,end,0)
#     print(ans)




n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))


def dfs(node, goal, acc):
  
    if node == goal:
        return acc

    for child, weight in tree[node]:
        if not visited[child]:
            visited[child] = 1
            result = dfs(child, goal, acc + weight)
            if result is not None:
                return result


for _ in range(m):
    start, end = map(int, input().split())
    visited = [0 for _ in range(n + 1)]  
    visited[start] = 1
    ans = dfs(start, end, 0)
    print(ans)