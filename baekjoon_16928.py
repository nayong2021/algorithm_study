# https://www.acmicpc.net/problem/16928
import heapq
import sys

INF = sys.maxsize
N, M = map(int, input().split())

snake_and_ladder = {}

for _ in range(N+M):
    x, y = map(int, input().split())
    snake_and_ladder[x] = y

heap = []
board = [INF] * 101
board[1] = 0

heapq.heappush(heap, (0, 1))

while True:
    count, current = heapq.heappop(heap)
    if current == 100:
        break
    if count > board[current]:
        continue
    for i in range(1, 7):
        if current+i > 100:
            break
        next_position = current + i if current + i not in snake_and_ladder else snake_and_ladder[current+i]
        if board[next_position] > count + 1:
            board[next_position] = count+1
            heapq.heappush(heap, (count+1, next_position))
print(board[100])