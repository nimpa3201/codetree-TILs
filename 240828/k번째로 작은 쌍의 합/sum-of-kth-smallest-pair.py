import heapq

n,m,k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
pq = []

for i in range(n):
    num1 = arr1[i]
    for j in range(m):
        num2 = arr2[j]
        sum_val = num1 + num2
        
        if len(pq) < k:
            heapq.heappush(pq, -sum_val)
        else:
            if sum_val < -pq[0]:
                heapq.heapreplace(pq, -sum_val)
ans = -heapq.heappop(pq)
print(ans)