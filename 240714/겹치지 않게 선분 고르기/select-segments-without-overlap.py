n = int(input())
arr = list()
selected = [0 for _ in range(n)]
tmp =[]
result =0
ans = 0
for _ in range(n):
    x1,x2 = map(int,input().split())
    arr.append((x1,x2))
end =0


def select(arr,curr,num,temp):
    global end,ans
    if end ==len(arr)+1:
        return ans
    for i in range(len(arr)):
        if not selected[i]:
            if tmp[-1][1] < arr[i][0]:  
                selected[i]=1
                end+=1
                tmp.append(arr[i])
                select(arr,curr,num+1,temp)
                selected[i]=0
                tmp.pop()
        ans = max(ans,len(tmp))
    return ans    
    
    


for i in range(n):
    tmp =[]
    selected[i] =1
    tmp.append(arr[i])
    result = select(arr,i,0,tmp)
    selected[i]=0
    tmp.pop()
print(result)