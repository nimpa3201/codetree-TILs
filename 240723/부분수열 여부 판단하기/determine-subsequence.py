n, m = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

R = -1
for L in range(m):
    while R + 1 < n and arrB[L] != arrA[R + 1]:
        R += 1
    if R + 1 < n and arrB[L] == arrA[R + 1]:
        R += 1
    else:
        print("No")
        exit()

print("Yes")