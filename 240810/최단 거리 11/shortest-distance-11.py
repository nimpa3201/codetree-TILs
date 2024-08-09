import sys
import heapq

INF = int(1e9)
n, m = map(int, input().split())


graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)


for _ in range(m):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))


for i in range(1, n + 1):
    graph[i].sort()

a, b = map(int, input().split())


dist[b] = 0
pq = []
heapq.heappush(pq, (0, b))

while pq:
    d, v = heapq.heappop(pq)

    if dist[v] != d:
        continue

    for new_v, new_d in graph[v]:
        new_dist = dist[v] + new_d
        if new_dist < dist[new_v]:
            dist[new_v] = new_dist
            heapq.heappush(pq, (new_dist, new_v))


print(dist[a])


ptr = a
print(ptr, end=' ')
while ptr != b:
    for new_v, new_d in graph[ptr]:
        if dist[ptr] == dist[new_v] + new_d:
            ptr = new_v
            break
    print(ptr, end=' ')