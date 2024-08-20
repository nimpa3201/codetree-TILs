n, k = map(int, input().split())  # n은 사람 수, k는 사진 크기
max_dot = 0
arr = []

for _ in range(n):
    dot, alph = input().split()
    dot = int(dot)
    if dot > max_dot:
        max_dot = dot
    arr.append((dot, alph))

photo = [0 for _ in range(max_dot + 1)]
for dot, alph in arr:
    if alph == "G":
        photo[dot] = 1
    else:
        photo[dot] = 2


if k > max_dot:
    ans = sum(photo)
else:
    ans = 0
    for i in range(max_dot - k + 1):
        tmp = 0
        for j in range(i, i + k+1):
            tmp += photo[j]
        ans = max(ans, tmp)

print(ans)