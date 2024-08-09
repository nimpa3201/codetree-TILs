n = int(input())
cmd =[]
arr = [ 0 for _ in range(100000)]
for _ in range(n):
    step,direct = input().split()
    step = int(step)
    cmd.append((step,direct))
start = 5000

for step,direct in cmd :
    if direct =="R":
        for i in range(start,start+step):
            arr[i] = 1 # 검
        start = start+step-1
    
    if direct =="L":
        for i in range(start,start-step,-1):
            arr[i] = -1 # 흰
        start = start-step+1
d= {-1:0,1:0}
for i in arr:
    if i ==-1:
        d[i]+=1
    elif i == 1:
        d[i]+=1
    else:
        continue
ans= d.values()
print(*ans)