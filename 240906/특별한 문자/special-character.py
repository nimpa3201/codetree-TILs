string = list((input()))

d = dict()

for i in string:
    if i not in d:
        d[i] =1
    else:
        d[i] +=1
flag = False        
for i in d:
    if d[i] ==1:
        flag = True
        print(i)
        break
if not flag:
    print("None")