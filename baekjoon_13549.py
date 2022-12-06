# https://www.acmicpc.net/problem/13549

import heapq
n, k = map(int, input().split())

def bfs(n):
    heap = []
    distances = [float("inf")] * 100001
    distances[n] = 0
    heapq.heappush(heap, (0, n))
    while heap:
        distance, current = heapq.heappop(heap)

        if current-1 >= 0 and distances[current-1] > distance + 1:
            distances[current-1] = distance + 1
            heapq.heappush(heap, (distance+1, current-1))
        if current+1 <= 100000 and distances[current+1] > distance + 1:
            distances[current+1] = distance + 1
            heapq.heappush(heap, (distance+1, current+1))
        if current*2 <= 100000 and distances[current*2] > distance:
            distances[current*2] = distance
            heapq.heappush(heap, (distance, current*2))
    return distances

result = bfs(n)
print(result[k])