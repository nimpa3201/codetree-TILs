n,m,k = map(int,input().split())  # m 번까지 , k개의말 , n번 턴
nums = list(map(int,input().split()))
cnt =0
ans =0
def choose(num,acc,cnt):
    if num ==n+1:
        print(cnt)
        return
    if acc >= m:
        cnt+=1

    for i in nums:
        acc+=i
        choose(num+1,acc,cnt)
        acc-=i
    return

choose(1,0,0)