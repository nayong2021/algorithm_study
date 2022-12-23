# https://www.acmicpc.net/problem/6497

import sys
sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline

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
    if a == b:
        return True, parent[a]
    if parent[a] > parent[b]:
        a, b = b, a
    parent[a] += parent[b]
    parent[b] = a
    return False, parent[a]
while True:
    m, n = map(int, input().split())
    parent = [-1] * m
    edges = []
    total_cost = 0
    if m == n == 0:
        break
    for _ in range(n):
        x, y, z = map(int, input().split())
        total_cost += z
        edges.append((z, x, y))
    edges.sort()
    saved_cost = 0
    for z, x, y in edges:
        is_union, child_num = union(x, y)
        if is_union:
            continue
        saved_cost+=z
        if -child_num == m:
            break
    print(total_cost - saved_cost)