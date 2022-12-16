#https://www.acmicpc.net/problem/1167

import sys

input = sys.stdin.readline

def dfs(start_node):
    stack = [start_node]
    dp = [-1] * (V+1)
    dp[start_node] = 0
    while stack:
        cur = stack.pop()
        for dest, cost in edges[cur]:
            if dp[dest] == -1:
                dp[dest] = cost + dp[cur]
                stack.append(dest)
    return dp

V = int(input())
edges = [[] for _ in range(V+1)]
for _ in range(1, V+1):
    E = list(map(int, input().split()))
    for i in range(1, len(E)-1, 2):
        edges[E[0]].append((E[i], E[i+1]))

start_from_1 = dfs(1)
start_node = start_from_1.index(max(start_from_1))
start_from_start_node = dfs(start_node)
print(max(start_from_start_node))