# https://www.acmicpc.net/problem/2213

import sys
sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline

n = int(input())
weight = [None] + list(map(int, input().split()))
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

included = [None] * (n+1)
not_included = [None] * (n+1)

def dfs_to_calc_independent_set(n, parent):
    max_weight_when_n_included = weight[n]
    max_weight_when_n_not_included = 0
    independent_set_when_n_included = [n]
    independent_set_when_n_not_included = []
    for child in edges[n]:
        if child == parent:
            continue
        dfs_to_calc_independent_set(child, n)
        max_weight_on_child_not_included, independent_set_when_child_not_included = not_included[child]
        max_weight_on_child_included, independent_set_when_child_included = included[child]
        max_weight_when_n_included += max_weight_on_child_not_included
        independent_set_when_n_included += independent_set_when_child_not_included
        if max_weight_on_child_included > max_weight_on_child_not_included:
            max_weight_when_n_not_included += max_weight_on_child_included
            independent_set_when_n_not_included += independent_set_when_child_included
        else:
            max_weight_when_n_not_included += max_weight_on_child_not_included
            independent_set_when_n_not_included += independent_set_when_child_not_included
    included[n] = (max_weight_when_n_included, independent_set_when_n_included)
    not_included[n] = (max_weight_when_n_not_included, independent_set_when_n_not_included)

dfs_to_calc_independent_set(1, None)

max_weight, independent_set = max(included[1], not_included[1])
independent_set.sort()
print(max_weight)
for i in independent_set:
    print(i, end=' ')