n, k, t  = input().split()
dic = []
n = int (n)
k = int(k)

for _ in range(n):
    dic.append(input())



flag = True
t_arr =[]
arr =[]
for elem in dic:
    for i in range(len(t)):
        if elem[i] ==t[i]:
            flag = True
        else:
            
            flag=False
    if flag:
        t_arr.append(elem)
    else:
        arr.append(elem)
t_arr.sort()
arr.sort()
ans = t_arr + arr
print(ans[k-1])