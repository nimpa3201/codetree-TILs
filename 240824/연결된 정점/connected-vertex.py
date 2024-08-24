n,m = map(int,input().split())
uf =[0]+[ i for i in range(1,n+1)]

def find(x):
    if uf[x] ==x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(X,Y):
    X,Y = find(X),find(Y)
    uf[X] = find(Y)

for _ in range(m):
    arr =list(input().split())
    if arr[0] == "x":
        union(int(arr[1]),int(arr[2]))
    else:
        cnt =0
        for i in uf:
            if i == uf[int(arr[1])] :
                cnt+=1
        print(cnt)