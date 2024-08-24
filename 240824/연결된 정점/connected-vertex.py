n,m = map(int,input().split())
uf =[ i for i in range(n+1)]
size =[1] * (n+1)

def find(x):
    if uf[x] ==x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x,y):
    X,Y = find(x),find(y)
    
    if X != Y:
        if size[X] < size[Y]:
            X,Y = Y,X
        uf[Y] = X
    size[X]+=size[Y]




for _ in range(m):
    arr =list(input().split())
    if arr[0] == "x":
        union(int(arr[1]),int(arr[2]))
    else:
        print(size[int(arr[1])])