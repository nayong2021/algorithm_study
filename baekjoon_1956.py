# https://www.acmicpc.net/problem/1956
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
costs = []
for i in range(V+1):
    costs.append([float("inf")] * (V+1))
for _ in range(E):
    a, b, c = map(int, input().split())
    if costs[a][b] > c:
        costs[a][b] = c

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])

min_cycle_cost = float("inf")

for i in range(1, V+1):
    min_cycle_cost = min(min_cycle_cost, costs[i][i])
print(min_cycle_cost if min_cycle_cost != float("inf") else -1)