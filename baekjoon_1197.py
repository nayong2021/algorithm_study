# https://www.acmicpc.net/problem/1197

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
        return True, parent[x]
    if parent[x] > parent[y]:
        x, y = y, x
    parent[x] += parent[y]
    parent[y] = x
    return False, parent[x]

V, E = map(int, input().split())
weight_sum = 0
parent = [-1] * (V+1)
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()
for C, A, B in edges:
    is_union, child_num = union(A, B)
    if is_union:
        continue
    weight_sum += C
    if -child_num == V:
        break
print(weight_sum)