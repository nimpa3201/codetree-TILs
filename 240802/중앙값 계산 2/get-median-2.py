n = int(input())
arr = list(map(int,input().split()))

for i in range(0,n+1):
    if i % 2 ==1:
        sort = arr[:i]
        sort.sort()
        print(sort[i//2],end =" ")