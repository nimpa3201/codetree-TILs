# 짝수 나누기2
# 홀수 곱하기3 더하기 1
num = int(input())
cnt =0
def fun(n):
    global cnt
    if n ==1:
        return cnt
    
    if n%2 ==0:
        cnt+=1
        return fun(n//2)
   

    else:
        cnt+=1
        return fun(3*n+1)
       
       
print(fun(3))