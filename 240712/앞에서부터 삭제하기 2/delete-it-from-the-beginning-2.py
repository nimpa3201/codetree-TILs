import heapq

n = int(input())
arr = list(map(int, input().split()))

s = 0
max_avg = 0
pq = []

heapq.heappush(pq, arr[n - 1])
s += arr[n - 1]

for i in range(n - 2, 0, -1):
    heapq.heappush(pq, arr[i])
    s += arr[i]

    min_num = pq[0]
    avg = (s - min_num) / (n - i - 1)

    if max_avg < avg:
        max_avg = avg

print(f"{max_avg:.2f}")