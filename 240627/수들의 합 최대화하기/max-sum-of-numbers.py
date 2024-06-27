n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def calculate_sum(perm, grid):
    total_sum = 0
    for i in range(n):
        total_sum += grid[i][perm[i]]
    return total_sum

def permutation(perm, chosen, grid, max_sum):
    if len(perm) == n:
        current_sum = calculate_sum(perm, grid)
        max_sum[0] = max(max_sum[0], current_sum)
        return
    
    for i in range(n):
        if not chosen[i]:
            perm.append(i)
            chosen[i] = True
            permutation(perm, chosen, grid, max_sum)
            perm.pop()
            chosen[i] = False

max_sum = [0]
chosen = [False] * n
perm= []
permutation(perm, chosen, grid, max_sum)

print(max_sum[0])