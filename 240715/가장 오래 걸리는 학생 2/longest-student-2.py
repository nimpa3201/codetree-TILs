import sys
import heapq
n,m = map(int,input().split())
INF = sys.maxsize
dist = [ INF for _ in range(n+1)]
edges = [[] for _ in range(n+1)]
pq =[]
for _ in range(m):
    a,b,d = map(int,input().split())
    edges[b].append((d,a))
    
def dijkstra(n):
    dist[n] =0
    heapq.heappush(pq,(0,n))
    
    while pq:
        
        min_dist,min_index = heapq.heappop(pq)
        
        if dist[min_index]!=min_dist:
            continue
        
        for target_dist,target_index in edges[min_index]:
            new_dist = target_dist+min_dist
            if new_dist < dist[target_index]:
                dist[target_index] = new_dist
                heapq.heappush(pq,(new_dist,target_index))
    return max(dist[1:])
        
result =dijkstra(n)
print(result)