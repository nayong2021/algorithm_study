# https://www.acmicpc.net/problem/11779
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

dp = [(INF, None)] * (n+1)
lines = []
for _ in range(n+1):
    lines.append([])

for _ in range(m):
    start, end, cost = map(int, input().split())
    lines[start].append((end, cost))

A, B = map(int, input().split())

dp[A] = (0, None)

heap = []

heapq.heappush(heap, (0, A))

while heap:
    dist, cur = heapq.heappop(heap)
    if dp[cur][0] < dist:
        continue
    for end, cost in lines[cur]:
        dist_to_end, _ = dp[end]
        if dist_to_end > dist + cost:
            dp[end] = (dist+cost, cur)
            heapq.heappush(heap, (dist+cost, end))
print(dp[B][0])
route = []
cur = B

while cur is not None:
    route.append(cur)
    _, cur = dp[cur]

print(len(route))
for i in route[::-1]:
    print(i, end = ' ')