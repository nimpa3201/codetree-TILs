import heapq
T = int(input())

for _ in range(T):
    m = int(input())
    arr = list(map(int, input().split()))
    pq1 = []
    pq2 = []

    for i in range(m):
        if len(pq1) == 0 or arr[i] <= -pq1[0]:
            heapq.heappush(pq1, -arr[i])
        else:
            heapq.heappush(pq2, arr[i])

        if len(pq1) > len(pq2) + 1:
            heapq.heappush(pq2, -heapq.heappop(pq1))
        elif len(pq2) > len(pq1):
            heapq.heappush(pq1, -heapq.heappop(pq2))

        if i % 2 == 0:
            print(-pq1[0],end =" ")
    print()