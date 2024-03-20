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
    if dx == 'R' :
        for i in range(step):
            Astep.append(Astep[idx]+1)
            idx +=1
    else:
        for i in range(step):
            Astep.append(Astep[idx]-1)
            idx +=1

idx =0
for dx , step in B :
    step = int(step)
    if dx == 'R' :
        for i in range(step):
            Bstep.append(Bstep[idx]+1)
            idx +=1
    else:
        for i in range(step):
            Bstep.append(Bstep[idx]-1)
            idx +=1

for i in range(len(Astep)):
    if Astep[i] == Bstep[i]!=0:
        print(i)
        break