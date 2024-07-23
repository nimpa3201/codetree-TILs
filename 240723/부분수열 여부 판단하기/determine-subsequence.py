n, m = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
R = 0 

for L in range(m):
    while R < n and arrB[L] != arrA[R]:
        R += 1
    if R == n:
        print("No")
        exit() 
    R += 1  

print("Yes")