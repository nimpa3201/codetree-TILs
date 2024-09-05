import heapq

n = int(input())
Bcard = [int(input()) for _ in range(n)]

Bcard_set = set(Bcard)
Acard = [i for i in range(1, 2 * n + 1) if i not in Bcard_set]

heapq.heapify(Acard)
heapq.heapify(Bcard)

cnt = 0
while Bcard:
    Belem = heapq.heappop(Bcard)
    
    while Acard and Acard[0] < Belem:
        heapq.heappop(Acard)
    
    if Acard:
        heapq.heappop(Acard)
        cnt += 1

print(cnt)