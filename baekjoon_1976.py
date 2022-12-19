#https://www.acmicpc.net/problem/1976

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

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
        return
    if parent[y] < parent[x]:
        x, y = y, x
    parent[x] += parent[y]
    parent[y] = x

N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
parent = [-1] * (N+1)

for i in range(1, N):
    for j in range(i+1, N+1):
        if graph[i-1][j-1]:
            union(i, j)

ancestor = find(plan[0])
is_possible = True

for city in plan:
    if ancestor != find(city):
        is_possible = False
        break
print('YES' if is_possible else 'NO')