n = int(input())
cmd = []
for _ in range(n):
    step,direct = input().split()
    step = int(step)
    cmd.append((step,direct))
arr = [[2,0,0] for _ in range(100000)]
start = 50000
for step,direct in cmd :
    if direct =="R":
        for i in range(start,start+step):
            arr[i][1]+=1
            if arr[i][1]>=2 and arr[i][2]>=2:
                arr[i][0] =0
            else:
                arr[i][0] =1 #검정

        start = start+step-1
    if direct =="L":
        for i in range(start,start-step,-1):
            arr[i][2]+=1
            if arr[i][1]>=2 and arr[i][2]>=2:
                arr[i][0] =0 #회색
            else:
                arr[i][0] =-1 #흰
        start = start-step+1
   
d= dict()
d ={ -1: 0, 1: 0, 0: 0}
for i , _, _ in arr:
    if i ==1:
        d[i]+=1
    elif i ==-1:
        d[i]+=1
    elif i ==0:
        d[i]+=1
    else:
        continue
ans = d.values()
print(*ans)
 # 흰 검 회색