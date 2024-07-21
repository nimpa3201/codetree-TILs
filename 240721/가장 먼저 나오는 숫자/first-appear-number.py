n,m = map(int,input().split())
arr = [0]+list(map(int,input().split()))
targets = list(map(int,input().split()))


def lower_bound(target):
    left,right = 0 , n-1
    min_idx = n

    while left <= right:
        mid = (left+right)//2

        if arr[mid]>= target:
            min_idx = min(min_idx,mid)
            right = mid -1
        
      
        else:
            left = mid +1
    return min_idx

for i in targets:
    if arr[lower_bound(i)] == i and lower_bound(i) <= n:
        print(lower_bound(i))
    else:
        print(-1)