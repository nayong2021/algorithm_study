# https://www.acmicpc.net/problem/12852

from collections import deque

N = int(input())

move = [0] * (N+1)

queue = deque([N])

while True:
    cur = queue.popleft()
    if cur == 1:
        break
    if cur % 3 == 0 and move[int(cur / 3)] == 0:
        move[int(cur / 3)] = cur
        queue.append(int(cur / 3))
    if cur % 2 == 0 and move[int(cur / 2)] == 0:
        move[int(cur / 2)] = cur
        queue.append(int(cur / 2))
    if move[cur - 1] == 0:
        move[cur - 1] = cur
        queue.append(cur - 1)


road = [1]
cur = 1
while cur != N:
    road.append(move[cur])
    cur = move[cur]

print(len(road) - 1)
for i in road[::-1]:
    print(i, end=' ')