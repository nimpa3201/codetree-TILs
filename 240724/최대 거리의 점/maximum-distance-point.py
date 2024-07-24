n,m = map(int,input().split())
dot = []
for _ in range(n):
    dot.append(int(input()))
dot.sort()
def is_possible(mid):
    pre = 0
    cnt =1
    for i in range(1,n):
       if dot[i] - dot[pre]>= mid:
            cnt+=1
            pre =i       
    return cnt >=m

left ,right ,ans = 0,max(dot),0

while left <= right:
    mid = (left + right)//2
    if is_possible(mid) :
        left = mid +1
        ans = max(ans,mid)
    else:
        right = mid-1
print(ans)