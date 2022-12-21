import sys
sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline
DUMMY = None
def find(a):
    if parent[a] < 0:
        return a
    else:
        ancestor = find(parent[a])
        parent[a] = ancestor
        return ancestor

def union(a, b):
    a = find(a)
    b = find(b)
    if a==b:
        return True, parent[a]
    if parent[a] > parent[b]:
        a, b = b, a
    parent[a] += parent[b]
    parent[b] = a
    return False, parent[a]

N, M = map(int, input().split())
coordinates = [DUMMY]
parent = [-1] * (N+1)
for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))
edges = []
for i in range(1, N+1):
    x1, y1 = coordinates[i]
    for j in range(i+1, N+1):
        x2, y2 = coordinates[j]
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        edges.append((dist, i, j))
edges.sort()
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)
total_cost = 0
for dist, a, b in edges:
    is_union, child_num = union(a, b)
    if is_union:
        continue
    total_cost += dist
    if -child_num == N:
        break
print("{:.2f}".format(total_cost))