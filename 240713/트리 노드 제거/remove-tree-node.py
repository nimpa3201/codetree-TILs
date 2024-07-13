n = int(input())
arr = list(map(int,input().split()))
remove = int(input())
tree = [[] for _ in range(n)]
visited= [0 for _ in range(n)]
def makeTree(parent):
    for i in range(len(parent)):
        if arr[i] ==-1:
            root = i
            continue
        tree[arr[i]].append(i)
    return tree ,root

tree = makeTree(arr)

def removeLeaf(parent):
    global remove,tree
    if parent ==remove:
        visited[remove]=0
    for node in tree[0][parent]:
        if not visited[node]:
            visited[node]=1
            removeLeaf(node)
    return visited
print(removeLeaf(tree[1]))