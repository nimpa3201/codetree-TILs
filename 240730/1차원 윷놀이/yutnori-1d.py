import sys
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

max_cnt = 0

def choose(num, acc, cnt):
    global max_cnt
    if acc >= m:
        cnt+=1
        acc=1
    
    
    if num == n+1:
        if cnt > max_cnt:
            max_cnt = cnt
        return
    
   
 
    for i in nums:
        acc+=i
        choose(num + 1, acc , cnt) 
        acc -= i
    
    

choose(1, 1, 0)
print(max_cnt)