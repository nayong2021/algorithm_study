# https://www.acmicpc.net/problem/1967

import sys

input = sys.stdin.readline

def dfs(start_node):
    stack = [start_node]
    dp = [-1] * (n+1)
    dp[start_node] = 0
    while stack:
        cur = stack.pop()
        for dest, cost in edges[cur]:
            if dp[dest] == -1:
                dp[dest] = cost + dp[cur]
                stack.append(dest)
    return dp

n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    start, dest, cost = map(int, input().split())
    edges[start].append((dest, cost))
    edges[dest].append((start, cost))
start_from_1 = dfs(1)
start_node = start_from_1.index(max(start_from_1))
start_from_start_node = dfs(start_node)
print(max(start_from_start_node))