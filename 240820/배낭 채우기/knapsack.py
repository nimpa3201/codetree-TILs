N, M = map(int,input().split()) # N 보석개수 ,M 보석 무게합  
stuff=[(0,0)]

for _ in range(N):
    weight , value = map(int,input().split())
    stuff.append((weight,value))

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight]+value)
print(dp[N][M])