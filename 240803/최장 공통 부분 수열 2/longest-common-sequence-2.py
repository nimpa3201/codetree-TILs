A = input()
B = input()

len_a= len(A)
len_b = len(B)

dp = [[0 for _ in range(len_b+1)] for _ in range(len_a+1)]
ans =[]
for i in range(1,len_a+1):
    for j in range(1,len_b+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else: 
            if dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
def find_text(r,c):
    if r ==0 or c ==0:
        return
    if A[r-1] == B[c-1]:
        ans.append(A[r-1])
        find_text(r-1,c-1)
    else:
        if dp[r-1][c]> dp[r][c-1]:
            find_text(r-1,c)
        else:
            find_text(r,c-1)

find_text(len_a,len_b)
ans = ans[::-1]

for i in ans:
    print(i,end="")