import sys
import heapq
INF = sys.maxsize
n,m,x = map(int,input().split())
start_to_x = [[] for _ in range(n+1)]
x_to_star = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]

for _ in range(m):
    a,b,w = map(int,input().split())
    start_to_x[b].append((w,a))
    x_to_star[a].append((w,b))
    
    
def dijkstra(end,edges):
    pq =[]
    dist[end] = 0
    heapq.heappush(pq,(0,end))
    
    while pq :
        min_dist,min_index =heapq.heappop(pq)
        
        if dist[min_index] != min_dist:
            continue
        
        for target_dist,target_index in edges[min_index]:
            new_dist = min_dist + target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(pq,(new_dist,target_index))
    return dist
    
result1=dijkstra(x,start_to_x)
dist = [INF for _ in range(n+1)]
result2=dijkstra(x,x_to_star)
ans =0
for i ,j in zip(result1[1:],result2[1:]):
    ans = max(ans,i+j)
print(ans)