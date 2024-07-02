n = int(input())
town = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] *n for _ in range(n)]
dirs={0 :(0,1) , 1 : (1,0), 2: (-1,0), 3: (0,-1) } #오른쪽, 아래 , 위 ,왼쪽
ans =[]
def dfs(x,y):
    global person_num
    arr=[]
    for i in range(4):
        nx = x + dirs[i][0]
        ny = y + dirs[i][1]

        if 0<= nx <n and 0<= ny < n and not visited[nx][ny] and town[nx][ny]==1:
            visited[nx][ny]=1
            person_num +=1
            dfs(nx,ny)
          
            
         


for i in range(n):
    for j in range(n):
        if 0<=i<n and 0<=j<n and visited[i][j] ==0 and town[i][j] ==1:
            person_num=1
            visited[i][j]=1
            dfs(i,j)
            ans.append(person_num)
print(len(ans))
ans.sort()
for i in ans:
    print(i)