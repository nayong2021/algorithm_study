# https://www.acmicpc.net/problem/15681

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(n, parent):
    for child in edges[n]:
        if child != parent:
            memo[n] += dfs(child, n)
    return memo[n]

N, R, Q = map(int, input().split())

edges = [[] for i in range (N+1)]
memo = [1] * (N+1)

for _ in range(N-1):
    U, V = map(int, input().split())
    edges[U].append(V)
    edges[V].append(U)

dfs(R, None)

for _ in range(Q):
    U = int(input())
    print(memo[U])