n,m = map(int,input().split())
dictionary = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
path = [[0]*m for _ in range(n)]

x,y =0,0
path[x][y] = dictionary[0]

dirs = { 0: (-1,0), 1:(0,1), 2:(1,0),3:(0,-1) }

dir_num = 1


def is_range(x,y):
    return (0<=x<n and 0<=y<m) and path[x][y] ==0
        


for i in range(1,n*m):
    nx = x+dirs[dir_num][0]
    ny = y+dirs[dir_num][1]

    if is_range(nx,ny) :
        x, y = x + dirs[dir_num][0], y + dirs[dir_num][1]
        path[x][y] = dictionary[i%26]
       
        
        
    else:
        dir_num = (dir_num+1)%4
        x, y = x + dirs[dir_num][0], y + dirs[dir_num][1]
        path[x][y] = dictionary[i%26]
 
   
    


for alph in path:
    print(*alph)