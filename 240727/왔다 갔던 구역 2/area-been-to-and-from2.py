n = int(input())

cnt =0
arr = [0 for _ in range(23)]
start =10
for _ in range(n):
    step,direct = input().split()
    step = int(step)
    
    if direct =="R":
        for i in range(start+1,start+step+1):
            arr[i] +=1
        start = start+step+1

    if direct == "L":
        for i in range(start-1,start-step-1,-1):
            arr[i]+=1
        start = start-step-1
for i in range(len(arr)):
    if arr[i] >=2:
        cnt+=1
        
        
print(cnt)