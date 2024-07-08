n,m = map(int,input().split())
bomb = []

for _ in range(n):
    bomb.append(int(input()))
    
if m ==1:
    print(0) 
    exit()   


def remove(board,arr,k):
    for r in range(len(k)):
        for i in range(k[r][1]-arr[k[r][1]][1]+1,n):
            if board[i] == k[r][0]:
                board[i] =0
    temp  = [0] * n
    temp_idx = 0
    for i in range(n):
        if board[i] != 0:
            temp[temp_idx] = board[i]
            temp_idx+=1
    board = temp
    return board




def numPow(arr,k):  #터질 숫자 리턴해줌
    global bomb
    numIdx=[]
    for num,cnt,idx in arr:
        if cnt >=k: 
            numIdx.append((num,idx))
    return numIdx



def countSequence(arr): # 연속되는 것 세는 함수
    cnt =0
    prev = arr[0]
    store =[]
    for i in range(len(arr)):
        if prev == arr[i] and prev !=0:
            cnt+=1
            store.append((prev,cnt,i))
        else:
            cnt =1
            prev = arr[i]
            store.append((prev,cnt,i))
            
    return store


# arr1=countSequence(bomb)
# key =numPow(arr1,m) 
# result =remove(bomb,arr1,key)
# bomb = result
# print(bomb)



while True:

    arr1=countSequence(bomb)
    key =numPow(arr1,m) #처음 k 이상인 숫자와 인덱스 반환
    if key ==[]:
        break
    result =remove(bomb,arr1,key)
    bomb = result

ans =0
for i  in bomb:
    if i !=0:
        ans+=1

print(ans)

for i in range(ans):
    print(bomb[i])