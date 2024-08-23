N,M = map(int,input().split())
stuff = [(0,0)]
for _ in range(N):
    weight,value = map(int,input().split())
    stuff.append((weight,value))

dp = [[0 for _ in range(M+1) ] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if j >= stuff[i][0]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-stuff[i][0]]+stuff[i][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][M])