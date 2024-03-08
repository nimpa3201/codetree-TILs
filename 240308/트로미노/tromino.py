n,m = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(n)]
ans =0
def oneBythree(col,row):
    result =0
    for i in range(col,col+3):
        result += arr[i][row]
    return result

def threeByone(col,row):
    result =0
    for i in range(row,row+3):
        result +=arr[col][i]
    return result

def twoBytwo(col,row):
    result =0
    tmp =[]
    for i in range(col,col+2):
        for j in range(row,row+2):
            tmp.append(arr[i][j])
    tmp.sort(reverse=True)
    result = sum(tmp[:3])
    return result            


for col in range(n-2):
    for row in range(m):
        ans = max(ans,oneBythree(col,row))

for col in range(n):
    for row in range(m-2):
        ans = max(ans,threeByone(col,row))

for col in range(n-1):
    for row in range(m-1):
        ans = max(ans,twoBytwo(col,row))
print(ans)