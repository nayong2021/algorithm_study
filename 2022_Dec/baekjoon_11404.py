# https://www.acmicpc.net/problem/11404
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
costs = []
for i in range(n+1):
    costs.append([float("inf")] * (n+1))
    costs[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if costs[a][b] > c:
        costs[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(costs[i][j] if costs[i][j] != float("inf") else 0, end=' ')
    print('')