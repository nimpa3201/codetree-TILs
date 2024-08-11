import sys
import heapq
n,m = map(int,input().split())

nodes = {i for i in range(1,n+1)}
arr =set(map(int,input().split()))
arr1 = list(arr)
nodes = nodes-arr

INF = sys.maxsize
graph = [[] for _ in range(n+1) ]
dist = [INF for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))



def initialize():
    global dist
    dist = [INF for _ in range(n+1)]

def dijkstra(start):
    pq =[]
    heapq.heappush(pq,(0,start))
    while pq :
        min_dist,min_index = heapq.heappop(pq)
        if dist[min_index] != min_dist:
            continue
        
        for target_dist,target_index in graph[min_index]:
            new_dist = min_dist+target_dist
            if new_dist < dist[target_index]:
                dist[target_index] = new_dist
                heapq.heappush(pq,(new_dist,target_index))
    return min(dist[arr1[0]],dist[arr1[1]],dist[arr1[2]])
    
ans =-1
for start in nodes:
    initialize()
    dist[start] =0
    ans = max(ans,dijkstra(start))
print(ans)