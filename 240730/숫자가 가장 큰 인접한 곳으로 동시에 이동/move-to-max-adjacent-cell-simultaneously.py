n,m,t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
count = [[ 0 for _ in range(n)] for _ in range(n) ] 
nextcount = [[ 0 for _ in range(n)] for _ in range(n) ]


def move():
    global nextcount 
    # 상하좌우
    dirs = { 0 :(-1,0) , 1 :(1,0), 2:(0,-1), 3:(0,1)}

    # 전체를 탐색하면서
    for i in range(n):
        for j in range(n):
            # 만약 구슬이 있다면
            if count[i][j] == 1:
                x, y = i, j
                max_val =0

                # 네 방향 탐색
                for k in range(4):
                    nx = x + dirs[k][0]
                    ny = y + dirs[k][1]

                    # 범위 내부라면
                    if 0<=nx<n and 0<=ny<n:

                        if max_val < arr[nx][ny]:
                            max_val = arr[nx][ny]
                            pos_x,pox_y = nx,ny
                nextcount[pos_x][pox_y] += 1
    copy()
    nextcount = [[ 0 for _ in range(n)] for _ in range(n) ] 
    

def copy():
    global nextcount
    for i in range(n):
        for j in range(n):
            count[i][j] = nextcount[i][j]

def remove():
    for i in range(n):
        for j in range(n):
            if count[i][j] >=2:
                count[i][j] =0
          
def simulation():
    move()
    remove()

for _ in range(m):
    r,c = map(int,input().split())
    count[r-1][c-1] = 1

for _ in range(t):
    simulation()

ans = 0
for i in range(n):
    for j in range(n):
        ans +=count[i][j]
        
print(ans)