n, m = map(int, input().split())

def comb(start, cnt, ans):
    if cnt == m:
        print(*ans)
        return
    for i in range(start, n+1):
        ans.append(i)
        comb(i+1, cnt+1, ans)
        ans.pop()

comb(1, 0, [])