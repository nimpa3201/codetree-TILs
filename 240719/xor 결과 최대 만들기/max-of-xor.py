n, m = map(int,input().split())  # m개 숫자 뽑아 결과값 최대
arr = list(map(int,input().split()))
result =0
def comb(s,cnt,tmp,ans):
    global result
    if cnt == m:
        for i in tmp:
            ans^=i
    for i in range(s, n):
        tmp.append(arr[i])
        comb(s+1,cnt+1,tmp,ans)
        tmp.pop()
    result = max(result,ans)


comb(0,0,[],1)
print(result)