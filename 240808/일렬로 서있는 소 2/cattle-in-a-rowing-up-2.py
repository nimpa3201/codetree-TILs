# 백트랙킹
n = int(input())
arr = list(map(int,input().split()))
visited = [ 0 for _ in range(n)]
ans =[]
result =0
def permutation(start,num):
    global result
    max_num =0
    cnt =0
    if num == 3:
        for i in ans:
            if i >= max_num:
                max_num = i
                cnt+=1
        if cnt== 3:
            result+=1
        return

    for i in range(start,n):
        if not visited[i]:
            ans.append(arr[i])
            visited[i] =1
            permutation(i+1,num+1)
            ans.pop()
            visited[i]=0
    
permutation(0,0)

print(result)