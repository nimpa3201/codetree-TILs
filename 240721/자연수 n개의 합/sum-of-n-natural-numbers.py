s= int(input())

def is_possible(num):
    return num * (num+1)//2 <= s

left,right,max_num = 1,s,0

while left <= right:
    mid = (left+right)//2
    if is_possible(mid):
        left = mid+1
        max_num = max(max_num,mid)
    
    else:
        right = mid-1
print(max_num)