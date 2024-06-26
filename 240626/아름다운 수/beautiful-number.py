N = int(input())
output = 0
ans = []

def find_num(k, ans):
    global output

    if k == N:
        output += count_num(ans)
    else:
        for i in range(1, 5):
            ans.append(i)
            find_num(k+1, ans)
            ans.pop()

def count_num(lst):
    i = 0
    
    while i < len(lst):
        j = i + lst[i]
        if lst[i:j] != [lst[i]]*lst[i]:
            return 0
        i = j
    return 1

find_num(0, list())
print(output)