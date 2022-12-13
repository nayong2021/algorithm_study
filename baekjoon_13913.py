#https://www.acmicpc.net/problem/13913
from collections import deque

N, K = map(int, input().split())

road = [-1] * 100001
road[N] = -2
queue = deque([N])

while True:
    current = queue.popleft()
    if current == K:
        break
    for i in (current-1, current+1, 2*current):
        if 0 <= i <= 100000 and road[i] == -1:
            road[i] = current
            queue.append(i)
    
route = []
current = K
while current != -2:
    route.append(current)
    current = road[current]

print(len(route)-1)
for i in route[::-1]:
    print(i, end=' ')