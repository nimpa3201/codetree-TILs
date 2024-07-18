n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][n-1] = arr[0][n-1]

def initialize():
    for i in range(n-2,-1,-1):
        dp[0][i] = dp[0][i+1] + arr[0][i] 
        dp[n-1-i][n-1] = dp[n-i-2][n-1] + arr[n-1-i][n-1]
initialize()


for i in range(1,n):
    for j in range(n-2,-1,-1):
        dp[i][j] = min(dp[i-1][j]+arr[i][j],dp[i][j+1]+arr[i][j])

print(dp[n-1][0])