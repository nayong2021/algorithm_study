# https://www.acmicpc.net/problem/2533

import sys
sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline

def dfs(n, parent):
    min_early_adopter_when_n_included = 1
    min_early_adopter_when_n_not_included = 0
    for child in edges[n]:
        if child == parent:
            continue
        min_early_adopter_when_child_included, min_early_adopter_when_child_not_included = dfs(child, n)
        min_early_adopter_when_n_not_included += min_early_adopter_when_child_included
        min_early_adopter_when_n_included += min(min_early_adopter_when_child_included, min_early_adopter_when_child_not_included)
    return min_early_adopter_when_n_included, min_early_adopter_when_n_not_included
N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
print(min(dfs(1, None)))