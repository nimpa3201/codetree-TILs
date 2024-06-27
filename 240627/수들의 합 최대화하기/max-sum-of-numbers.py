n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
visited1 = [0 for _ in range(n) ]
visited2 = [0 for _ in range(n)] 
ans =[]
result =0
def maxNum(k):
    global ans,result
    if k == n:
        result = max(result,sum(ans))
    
    for i in range(n):
        for j in range(n):
            if not visited1[i] and not visited2[j] and i !=j :
                ans.append(grid[i][j])
                visited1[i]=1
                visited2[j]=1
                maxNum(k+1)
                ans.pop()
                visited1[i]=0
                visited2[j]=0
    return result
               

                
print(maxNum(0))