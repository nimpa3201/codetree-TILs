import sys
n = int(input())
dots=[]
for _ in range(n):
    x,y = map(int,input().split())
    dots.append((x,y))
ans = sys.maxsize
for i in range(n):
    for j in range(i+1,n):
        ans = min(ans,(dots[i][0] - dots[j][0])**2 + (dots[i][1] - dots[j][1])**2)
print(ans)