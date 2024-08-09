n,m,k = map(int,input().split()) #n명 k번이상 ,m번학생 번호
student = []
d = {i:0 for i in range(1,n+1)}
for _ in range(m):
    student.append(int(input()))
Flag = True
for i in student:
    d[i]+=1
    if d[i] >= k:
        print(i)
        Flag =False
        break
if Flag:
    print(-1)