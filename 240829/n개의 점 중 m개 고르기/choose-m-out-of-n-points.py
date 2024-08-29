n, m = map(int, input().split())
coordinates = []
ans = []

for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))


# m개의 점을 뽑고 나면, 뽑힌 점들 중에서 가장 최대인 거리를 찾습니다
def findTwoCoordinates(curr):
    largest = 0
    for i in range(len(curr)):
        x1, y1 = curr[i]
        for j in range(1, len(curr)):
            x2, y2 = curr[j]
            largest = max(largest, (x2-x1)**2 + (y2-y1) ** 2)
    return largest


minVal = float('inf')

def backtrack(index, cnt):
    global minVal
    if cnt == m:
        minVal = min(minVal, findTwoCoordinates(ans))
        return 
    
    for i in range(index, n):
        ans.append(coordinates[i])
        backtrack(i+1, cnt+1)
        ans.pop()
      

backtrack(0, 0)

print(minVal)