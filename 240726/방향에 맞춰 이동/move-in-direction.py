n = int(input())
cmd =[]
for _ in range(n):
    diretion, step  = map(str,input().split())
    step = int (step)
    cmd.append((diretion,step))


dirs = {'W' : (0,-1) , 'S' : (-1,0), 'N':(1,0) , 'E':(0,1)}
x, y = 0,0
for diretion, step in cmd :
    for _ in range(step):
        x+= dirs[diretion][0]
        y+= dirs[diretion][1]
print(y,x)