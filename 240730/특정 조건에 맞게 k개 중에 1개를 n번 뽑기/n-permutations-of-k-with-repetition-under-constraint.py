k,n = map(int,input().split()) #k 이하의 숫자, n 번 뽑기
ans =[]


def choose(num):
    if num ==n+1:
        print(*ans)
        return

    for i in range(1,k+1):
        if len(ans)>=2 and ans[-1] ==ans[-2] == i:
            continue
        ans.append(i)
        choose(num+1)
        ans.pop()


choose(1)