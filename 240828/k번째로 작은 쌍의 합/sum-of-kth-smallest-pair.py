import heapq
n,m,k = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
pq =[]

for i in range(n):
    num1 = arr1[i]
    for j in range(m):
        num2 = arr2[j]   
        heapq.heappush(pq,num1+num2)

for i in range(k):
   ans = heapq.heappop(pq)
print(ans)