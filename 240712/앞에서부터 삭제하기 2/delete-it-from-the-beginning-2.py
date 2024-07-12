import heapq
n = int(input())
arr = list(map(int,input().split()))
pq =[]
ans =0
for i in range(n-1,-1,-1):
    heapq.heappush(pq,(arr[i]))
    if i < n-2:
        heapq.heappop(pq)
    ans = max(ans,sum(pq)/len(pq))
a= "{:.2f}".format(ans)
print(a)