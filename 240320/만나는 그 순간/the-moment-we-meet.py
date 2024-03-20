n,m =map(int,input().split())
A = []
B = []
Astep = [0]
Bstep= [0]
for _ in range(n):
    A.append((input().split()))

for _ in range(m):
    B.append((input().split()))
idx =0
for dx , step in A :
    step = int(step)
    print(dx,step,idx)
    if dx == 'R' :
        for i in range(idx,idx+step):
            print(i)
            Astep.append(Astep[i]+1)
        idx = step
       
    else:
        for i in range(idx,step,-1):
           Astep.append(Astep[i]-1)
        idx +=i
print(Astep)