import sys

input = sys.stdin.readline

N, M = map(int, input().split())

routes = []

for _ in range(M):
    a, b, c = map(int, input().split())
    routes.append((a,b,c))

distances = [float("inf")] * (N+1)
distances[1] = 0

is_negative_cycle = False

for _ in range(N-1):
    for i in range(M):
        a, b, c = routes[i]
        if distances[b] > distances[a] + c:
            distances[b] = distances[a] + c
for i in range(M):
    a, b, c = routes[i]
    if distances[b] > distances[a] + c:
        is_negative_cycle = True
        break

if is_negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        print(distances[i] if distances[i] != float("inf") else -1)