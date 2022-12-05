# https://www.acmicpc.net/problem/1753

import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

init_vertex = int(input())

edges = [[] for i in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

distances = [float("inf") for i in range(V+1)]
distances[init_vertex] = 0

heap=[]
heapq.heappush(heap,(0, init_vertex))

while heap:
    distance, u = heapq.heappop(heap)

    if distances[u] < distance:
        continue

    for v, w in edges[u]:
        if distances[v] > distances[u] + w:
            distances[v] = distances[u] + w
            heapq.heappush(heap,(distances[u] + w, v))

for i in range(1, V+1):
    print("INF" if distances[i] == float("inf") else distances[i])