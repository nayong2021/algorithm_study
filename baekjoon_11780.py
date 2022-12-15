import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

costs = []
routes = []
for i in range(n+1):
    costs.append([INF] * (n+1))
    routes.append([''] * (n+1))
    costs[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if costs[a][b] > c:
        costs[a][b] = c
        routes[a][b] = (b, )

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if costs[j][i] + costs[i][k] < costs[j][k]:
                costs[j][k] = costs[j][i] + costs[i][k]
                routes[j][k] = routes[j][i] + routes[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(costs[i][j] if costs[i][j] != INF else 0, end=' ')
    print('')

for i in range(1, n+1):
    for j in range(1, n+1):
        if len(routes[i][j]) == 0:
            print(0)
        else:
            routes[i][j] = (i, ) + routes[i][j]
            print(len(routes[i][j]), end = ' ')
            for item in routes[i][j]:
                print(item, end = ' ')
            print('')