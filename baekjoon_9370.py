# https://www.acmicpc.net/problem/9370

import heapq

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    roads = [[] for i in range(n+1)]
    candidates = []
    for i in range(m):
        a, b, d = map(int, input().split())
        roads[a].append((b, d))
        roads[b].append((a, d))
    def dijkstra(n, s):
        heap = []
        heapq.heappush(heap, (0, s))
        distances = [float("inf")] * (n+1)
        distances[s] = 0
        while heap:
            distance, current = heapq.heappop(heap)
            if distance > distances[current]:
                continue
            for b, d in roads[current]:
                if distance + d < distances[b]:
                    distances[b] = distance + d
                    heapq.heappush(heap, (distance + d, b))
        return distances
    for i in range(t):
        candidates.append(int(input()))
    distances_from_s = dijkstra(n, s)
    distances_from_g = dijkstra(n, g)
    distances_from_h = dijkstra(n, h)
    distances_through_gh = [0]*(n+1)
    for i in range(1, n+1):
        distance_from_s_to_g = distances_from_s[g] + distances_from_g[h] + distances_from_h[i]
        distance_from_s_to_h = distances_from_s[h] + distances_from_h[g] + distances_from_g[i]
        distances_through_gh[i] = min(distance_from_s_to_g, distance_from_s_to_h)
    candidates.sort()
    for i in candidates:
        if distances_through_gh[i] == distances_from_s[i] and distances_through_gh[i] != float("inf"):
            print(i, end=' ')
    print('')
    