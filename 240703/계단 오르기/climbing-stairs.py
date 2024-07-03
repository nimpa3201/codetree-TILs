n = int(input())

dp = [0 for _ in range(n+1)]

if n <=4:
    print(1)
else:
    dp[2]=1
    dp[3]=1
    dp[4]=1

    for i in range(5,n+1):
        dp[i] = dp[i-2]+dp[i-3]
    print(dp[n])