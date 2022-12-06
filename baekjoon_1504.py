# https://www.acmicpc.net/problem/1504

import sys
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())

edges = [[] for i in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
v_1, v_2 = map(int, input().split())
def dijkstra(n, N):
    distances = [float("inf") for i in range(N+1)]
    distances[n] = 0
    heap=[]
    heapq.heappush(heap,(0, n))

    while heap:
        distance, u = heapq.heappop(heap)

        if distances[u] < distance:
            continue

        for v, w in edges[u]:
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                heapq.heappush(heap,(distances[u] + w, v))
    return distances

distances_from_1 = dijkstra(1, N)
distances_from_n = dijkstra(N, N)
distances_from_v1 = dijkstra(v_1, N)
distances_from_v1_to_v2 = distances_from_v1[v_2]

total_when_1_to_v1 = distances_from_1[v_1] + distances_from_v1_to_v2 + distances_from_n[v_2]
total_when_1_to_v2 = distances_from_1[v_2] + distances_from_v1_to_v2 + distances_from_n[v_1]

total = min(total_when_1_to_v1, total_when_1_to_v2)

print(total if total != float("inf") else -1)