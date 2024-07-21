n,m = map(int,input().split())
arr = list(map(int,input().split()))
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
    return min_idx+1

for i in targets:
    ans =lower_bound(i)
    print(ans if  ans < n-1 else -1)