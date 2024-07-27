n = int(input())
k = int(input())

def is_possible(num):
    cnt=0
    for i in range(1,n+1):
        cnt+=min(n,(num-1)//i)
    return cnt

left,right,ans = 1,n*n,0
while left<=right:
    mid = (left+right)//2
    if is_possible(mid) <= k-1:
        ans = max(ans,mid)
        left = mid +1
    else:
        right = mid -1
print(ans)