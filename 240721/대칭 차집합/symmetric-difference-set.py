a,b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
ans =len(A-B)+len(B-A)
print(ans)