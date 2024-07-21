n,k = map(int,input().split())
nums = list(map(int,input().split()))
d= dict()
for i in nums:
    if i not in d:
        d[i] =1
    else:
        d[i] +=1
d = sorted(d.items(),key = lambda x : (-x[1],-x[0]))


for i in range(k):
    print(d[i][0],end =" ")