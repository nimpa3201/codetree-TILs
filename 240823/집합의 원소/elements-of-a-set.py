import sys
n,m = map(int,input().split())
parent = [0]+[i for i in range(1,n+1)]

def find_parent(x) :
    if parent[x] !=x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b :
        parent[a] =b
    else:
        parent[b] =a


for _ in range(m):
    cmd,a,b = map(int,input().split())

    if cmd ==0 :
        union_parent(a,b)
    if cmd == 1:
        if find_parent(a) == find_parent(b):
            print(1)
        else:
            print(0)