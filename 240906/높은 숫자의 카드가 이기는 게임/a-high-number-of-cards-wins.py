import heapq
n = int(input())
Bcard = [int(input()) for _ in range(n)]

Acard = list()
for i in range(1,2*n+1):
    if i not in Bcard:
        Acard.append(i)
Apq =[]
Bpq =[]
for i in range(n):
        heapq.heappush(Apq,Acard[i])
        heapq.heappush(Bpq,Bcard[i])

Belem= heapq.heappop(Bpq)
cnt =0
while True :
        Aelem = heapq.heappop(Apq)
        if Belem< Aelem:
                cnt +=1
                if len(Bpq) >0 and len(Apq)>0:
                        Belem = heapq.heappop(Bpq)
                else:
                        break

print(cnt)