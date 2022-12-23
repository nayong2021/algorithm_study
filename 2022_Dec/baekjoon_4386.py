# https://www.acmicpc.net/problem/4386
import sys
sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline

def find(a):
    if parent[a]<0:
        return a
    else:
        ancestor=find(parent[a])
        parent[a]=ancestor
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

n = int(input())
stars = []
edges = []
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))
for i in range(n):
    x1, y1 = stars[i]
    for j in range(i+1, n):
        x2, y2 = stars[j]
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        edges.append((dist, i, j))
parent = [-1] * n
edges.sort()
total_cost = 0
for dist, a, b in edges:
    is_union, child_num = union(a, b)
    if is_union:
        continue
    total_cost+=dist
    if -child_num == n:
        break
print(total_cost)