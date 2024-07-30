# n = n번의 턴
# m = 1-m 까지 
# k 말의수

N,m,k=map(int,input().split())
nums =list(map(int,input().split()))
player = [1]*k
ans =0
def play (n):
    global ans
    if n==N:
        count=0
        for t in player:
            if t >= m :
                count +=1
        ans = max(ans,count)
        # print(count)
        return 
    
    for i in range (k):
        player[i]+= nums[n]
        play(n+1)
        player[i]-=nums[n]
    
play(0)
print(ans)