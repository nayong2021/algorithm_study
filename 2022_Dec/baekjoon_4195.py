# https://www.acmicpc.net/problem/4195
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if type(parent[x]) is not str and parent[x] < 0:
        return x
    else:
        ancestor = find(parent[x])
        parent[x] = ancestor
        return ancestor
def union(x, y):
    x = find(x)
    y = find(y)
    if x==y:
        return parent[x]
    else:
        if parent[x] < parent[y]:
            x, y = y, x
        parent[x] += parent[y]
        parent[y] = x
        return parent[x]

T = int(input())

for _ in range(T):
    F = int(input())
    parent = {}
    for i in range(F):
        x, y = input().split()
        parent[x] = parent.get(x, -1)
        parent[y] = parent.get(y, -1)
        print(-union(x,y))
