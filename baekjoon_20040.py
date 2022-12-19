import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if parent[x] < 0:
        return x
    else:
        ancestor = find(parent[x])
        parent[x] = ancestor
        return ancestor

def union(x, y):
    x = find(x)
    y = find(y)
    if x==y:
        return True
    if parent[x] > parent[y]:
        x, y = y, x
    parent[x] += parent[y]
    parent[y] = x
    return False

n, m = map(int, input().split())
parent = [-1] * n
for i in range(1, m+1):
    x, y = map(int, input().split())
    if union(x, y):
        print(i)
        exit()
print(0)