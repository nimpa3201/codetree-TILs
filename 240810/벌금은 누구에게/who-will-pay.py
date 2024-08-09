n,m,k = map(int,input().split()) #n명 k번이상 ,m번학생 번호
student = []
arr = [0 for _ in range(n+1)]
for _ in range(m):
    student.append(int(input()))
Flag = True
for i in student:
    arr[i]+=1
    if arr[i] >= k:
        print(i)
        Flag =False
        break
if Flag:
    print(-1)