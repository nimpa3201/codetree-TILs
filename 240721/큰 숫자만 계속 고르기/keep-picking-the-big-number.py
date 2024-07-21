import heapq
n,m = map(int,input().split())
arr =list(map(int,input().split()))
pq =[]
for i in arr:
    heapq.heappush(pq,-i)


for _ in range(m):
    num = heapq.heappop(pq)
    heapq.heappush(pq,num+1)
print(-min(pq))