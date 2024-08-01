import sys
n = int(input())
town = list(map(int,input().split()))
min_val =  sys.maxsize

for i in range(n):
    ans =0
    for j in range(n):
        ans +=town[j] *abs((j-i))
    min_val = min(min_val,ans)
print(min_val)