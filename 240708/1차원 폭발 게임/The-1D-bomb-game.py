n,m = map(int,input().split())
bomb = []

for _ in range(n):
    bomb.append(int(input()))
    
if m ==1:
    print(0) 
    exit()   


def remove(board,arr,k):
    for i in range(k[1]-arr[k[1]][1]+1,n):
        if board[i] == k[0]:
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

    numIdx=()
    global bomb 
    for num,cnt,idx in arr:
        if cnt >=k: 
            numIdx =(num,idx)
            return numIdx
    return -1



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






while True:

    arr1=countSequence(bomb)
    key =numPow(arr1,m) #처음 k 이상인 숫자와 인덱스 반환
    if key ==-1:
        break
    result =remove(bomb,arr1,key)
    bomb = result



ans =0
for i  in result:
    if i !=0:
        ans+=1

print(ans)

for i in range(ans):
    print(result[i])