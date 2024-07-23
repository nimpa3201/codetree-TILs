n,m =map(int,input().split())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))
R = -1
for L in range(m):
    while R+1 < n and arrB[L] != arrA[R]:
        R+=1
        #print(arrB[L],arrA[R])
        if arrB[L] == arrA[R]:
            break
        
        else:
            R+=1
    if R ==n:
        print("No")
        exit()
print("Yes")