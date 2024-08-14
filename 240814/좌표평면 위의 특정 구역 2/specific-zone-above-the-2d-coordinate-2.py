n = int(input())
dots = []
for _ in range(n):
    s,e = map(int,input().split())
    dots.append((s,e))
ans =1e9
for i in range(n):
    dot =[]
    for j in range(n):
        if i == j :
            continue
        dot.append(dots[j])
    dot.sort(key = lambda x: x[0])
    line1 = dot[-1][0] - dot[0][0]
    dot.sort(key = lambda x : x[1])
    line2 = dot[-1][1] - dot[0][1]
    ans = min(ans,line1*line2)
print(ans)