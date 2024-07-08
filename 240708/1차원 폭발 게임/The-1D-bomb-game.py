n, m = map(int, input().split())
bomb = []

for _ in range(n):
    bomb.append(int(input()))

if m == 1:
    print(0)
    exit()

def remove(board, k):
    for num, idx in k:
        start_idx = idx - m + 1
        for i in range(start_idx, idx + 1):
            if i < len(board) and board[i] == num:
                board[i] = 0

    temp = [num for num in board if num != 0]
    return temp

def numPow(arr):
    # 연속된 숫자가 m개 이상인 숫자의 리스트 반환
    numIdx = []
    for i in range(len(arr)):
        if arr[i][1] >= m:
            numIdx.append((arr[i][0], arr[i][2]))
    return numIdx

def countSequence(arr):
    cnt = 1
    prev = arr[0]
    store = []
    for i in range(1, len(arr)):
        if prev == arr[i] and prev != 0:
            cnt += 1
        else:
            store.append((prev, cnt, i - 1))
            cnt = 1
            prev = arr[i]
    store.append((prev, cnt, len(arr) - 1))  
    return store

while True:
    arr1 = countSequence(bomb)
    key = numPow(arr1)  
    if not key:
        break
    bomb = remove(bomb, key)

ans = len(bomb)

print(ans)
for num in bomb:
    print(num)