n,m =map(int,input().split())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))
R = 0
for L in range(m):
    while R+1 < n and arrB[L] != arrA[R]:
        R+=1
        if R ==m:
            print("No")
            exit()
        else:
            R+=1
print("Yes")