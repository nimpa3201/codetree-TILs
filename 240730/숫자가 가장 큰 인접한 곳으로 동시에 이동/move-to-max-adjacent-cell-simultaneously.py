n,m,t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
count = [[ 0 for _ in range(n)] for _ in range(n) ] 
nextcount = [[ 0 for _ in range(n)] for _ in range(n) ] 
for _ in range(m):
    r,c = map(int,input().split())
    count[r-1][c-1] =1


def move():
    global nextcount
    dirs = { 0 :(-1,0) , 1 :(1,0), 2:(0,-1), 3:(0,1)}
    for i in range(n):
        for j in range(n):
            if count[i][j] ==1:
                x,y = i,j
                max_val =0             
                for i in range(4):
                    nx = x + dirs[i][0]
                    ny = y + dirs[i][1]
                    if 0<=nx<n and 0<=ny<n:
                        if max_val < arr[nx][ny]:
                            max_val = arr[nx][ny]
                            pos_x,pox_y = nx,ny
                nextcount[pos_x][pox_y] =1
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








for _ in range(t):
    simulation()
ans =0
for i in range(n):
    for j in range(n):
        ans +=count[i][j]
print(ans)