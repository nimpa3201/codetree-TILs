cmd =input()

dirs = {0:(0,-1), 1: (-1,0), 2 : (0,1), 3: (1,0) } #남, 서, 북, 동
x,y =0,0
direction = 2
for elem in cmd :
    if elem == "L":
        direction = (direction+3)%4
    

    if elem == "R":
        direction = (direction+1)%4

    if elem == "F":
        x+=dirs[direction][0]
        y+=dirs[direction][1]

print(x,y)