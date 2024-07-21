n,m = map(int,input().split())
arr =  list(map(int,input().split()))
targets =[]
for _ in range(m):
    targets.append(int(input()))

def binary_search(target):
    left,right = 0,n-1
    while left <= right:

        mid = (left+right) //2

        if arr[mid] == target:
            return mid+1
        if arr[mid] > target:
            right = mid -1
        else:
            left = mid +1
    return -1
for i in targets:
    ans = binary_search(i)
    print(ans)