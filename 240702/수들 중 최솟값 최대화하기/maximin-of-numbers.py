# 슈가코트 
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
max_num = 0
def select(arr,n,sel):
    global max_num
    ans =[]
    global grid
    for i in range(n):
        sel.append(grid[i][arr[i]])
    sel.sort()
    return sel[0]


def perm(k,n,arr):
    global max_num
    global visited
    if k ==n :
        result = select(arr,n,[])
        max_num = max(max_num,result)
       
    for i in range(n):
        if not visited[i]:
            arr.append(i)
            visited[i]=1
            perm(k+1,n,arr)
            arr.pop()
            visited[i] =0
    
            

perm(0,n,[])
print(max_num)