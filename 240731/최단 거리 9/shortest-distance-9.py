import sys
import heapq
from collections import deque
INF = sys.maxsize
n,m = map(int,input().split())
dist = [ INF for _ in range(n+1) ] 
graph = [[] for _ in range(n+1)]
pq =[]
visited = [0 for _ in range(n)]
for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))
start,end  = map(int,input().split())
dist[start] =0
heapq.heappush(pq,(0,start))


def dijkstra(end):
    while pq :
        min_dist,min_index =heapq.heappop(pq)
        
        if dist[min_index] != min_dist:
            continue
        
        
        for target_dist,target_index in graph[min_index]:
            new_dist = min_dist+target_dist
            if new_dist < dist[target_index] :
                dist[target_index] = new_dist
                heapq.heappush(pq,(new_dist,target_index))
    return dist[end]


ans =dijkstra(end)
print(ans)

def bfs(end):
    q = deque()
    path = [end]
    q.append(end)
    while q:
        x= q.popleft()
        if x == start:
            break
        graph[x].sort()
        for w,s in graph[x]:
            if not visited[s] and dist[s] == dist[x]-w:
                visited[s] =1
                q.append(s)
                path.append(s)
                break
    return path
path = bfs(end)
path.reverse()
print(*path)