n,m,k = map(int,input().split())
uf =[0]+[i for i in range(1,n+1)]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(a,b):
    A,B = find(a),find(b)
    uf[A] = B


for _ in range(m):
    x,y = map(int,input().split())
    union(x,y)

arr = list(map(int,input().split()))

Flag = True
for i in range(k-1):
    if find(arr[i]) == find(arr[i+1]):
        Flag = True
        
    else:
        Flag = False
        break
if Flag:
    print(1)
else:
    print(0)