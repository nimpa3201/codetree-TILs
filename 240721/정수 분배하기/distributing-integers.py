n,m = map(int,input().split()) # 같은 크기의 정수 k를 m개 만든다. k의 최대값 (11개 이상)
arr=[]
for _ in range(n):
    arr.append(int(input()))


def is_possible(k):
    num =0
    for elem in arr:
        num+=elem//k
    return num>= m

left,right,ans = 1,max(arr),0

while left <= right:
    mid = (left+right)//2
    if is_possible(mid):
        left = mid+1
        ans = max(ans,mid)
    else:
        right = mid-1
print(ans)