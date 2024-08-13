n = int(input())
arr = [0]+list(map(int,input().split()))
arr.sort()
group=[]
for i in range(1,n+1):
    group.append(arr[i]+arr[-i])
print(max(group))