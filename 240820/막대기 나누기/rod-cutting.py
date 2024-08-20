N = int(input())
arr = [0]+list(map(int,input().split()))
stuff =[(0,0)]
for i in range(1,len(arr)):
    stuff.append((i,arr[i]))

dp =[[0 for _ in range(N+1)] for _ in range(N+1) ]

for i in range(1,N+1):
    for j in range(1,N+1):
        weight = stuff[i][0]
        value = stuff[i][1]
        
        if j >= weight :
            dp[i][j] = max(dp[i-1][j],dp[i][j-weight]+value)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][N])