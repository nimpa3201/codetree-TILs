n,t = map(int,input().split())
cmd = list(input())
score = [list(map(int,input().split()))for _ in range(n)]
# L 왼쪽으로 90도 / R 오른쪽으로 90도 / F 바라보는 방향으로 이동
dirs = { 0: (0,-1), 1:(-1,0), 2:(0,1), 3:(1,0) }
x,y = n//2,n//2
dir_num = 1
ans = score[x][y]

def is_range(x,y):
    return 0<=x<n and 0<=y<n


for i in cmd :
    if i =='R':
        dir_num = (dir_num+1)%4


    elif i =='L':
        dir_num = (dir_num+3)%4

    else:
        nx = x+dirs[dir_num][0]
        ny = y+dirs[dir_num][1]
        if is_range(nx,ny):
            ans += score[nx][ny]
            x= nx
            y =ny
print(ans)