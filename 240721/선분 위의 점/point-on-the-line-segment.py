n, m = map(int,input().split())
arr= list(map(int,input().split()))
arr.sort()

def lower_bound(target):
    left,right,min_idx = 0,n-1,n
    while left<= right:
        mid = (left+right)//2
        if arr[mid]>= target:
            right = mid-1
            min_idx = min(min_idx,mid)
        else:
            left = mid+1
    return min_idx

def upper_bound(target):
    left,right,min_idx = 0,n-1,n
    while left<= right:
        mid = (left+right)//2
        if arr[mid]> target:
            right = mid-1
            min_idx = min(min_idx,mid)
        else:
            left = mid+1
    return min_idx



for _ in range(m):
    v1, v2 = map(int,input().split())
    print(upper_bound(v2)-lower_bound(v1))