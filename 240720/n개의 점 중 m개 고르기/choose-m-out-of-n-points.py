n,m = map(int,input().split())
dots = []
result=0
ans =0
result1=20001
for _ in range(n):
    x,y = map(int,input().split())
    dots.append((x,y))



def select(start,cnt,arr,tmp):
    global result,ans,result1
    if cnt == m :
        result =0
        for i in range(len(tmp)):
            for j in range(i+1,len(tmp)):
               #print(tmp[i][0],tmp[i][1],tmp[j][0],tmp[j][1])
                ans = (tmp[i][0]-tmp[j][0])**2 + (tmp[i][1] -tmp[j][1])**2
        result = max(result,ans)
        result1 =min(result1,result)
    
        
        


            
    
            
        

    for i in range(start,len(arr)):
        tmp.append(arr[i])
        select(i+1,cnt+1,arr,tmp)
        tmp.pop()

select(0,0,dots,[])
print(result1)