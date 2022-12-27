# https://www.acmicpc.net/problem/17143

import sys
input=sys.stdin.readline

def move_shark(x, y):
    shark = sharks[fishing_area[y][x]]
    shark_speed, shark_direction = shark[speed], shark[direction]
    x_, y_ = x, y
    if shark_direction == UP:
        y_ = R - 1 - y_
        y_ += shark_speed
        if int(y_ / (R-1)) % 2:
            shark[direction] = DOWN
            y_ = R - 1 - (y_ % (R - 1))
        else:
            y_ %= (R - 1)
        y_ = R - 1 - y_
    elif shark_direction == DOWN:
        y_ += shark_speed
        if int(y_ / (R-1)) % 2:
            shark[direction] = UP
            y_ = R - 1 - (y_ % (R - 1))
        else:
            y_ %= (R - 1)
    elif shark_direction == LEFT:
        x_ = C - 1 - x_
        x_ += shark_speed
        if int(x_ / (C-1)) % 2:
            shark[direction] = RIGHT
            x_ = C - 1 - (x_ % (C - 1))
        else:
            x_ %= (C - 1)
        x_ = C - 1 - x_
    elif shark_direction == RIGHT:
        x_ += shark_speed
        if int(x_ / (C-1)) % 2:
            shark[direction] = LEFT
            x_ = C - 1 - (x_ % (C - 1))
        else:
            x_ %= (C - 1)
    fishing_area_after_move[y_][x_] = max(fishing_area_after_move[y_][x_], fishing_area[y][x], key=lambda x:sharks[x][size])
UP = 1; DOWN = 2; RIGHT = 3; LEFT = 4
direction = 1; speed = 2; size = 3

R, C, M = map(int, input().split())

fishing_area = [[0] * (C) for _ in range(R)]
sharks = [{size:0}]

for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    sharks.append({direction: d, speed: s, size: z})
    fishing_area[r-1][c-1] = i

total_catched = 0

for j in range(C):
    for i in range(R):
        if fishing_area[i][j]:
            total_catched += sharks[fishing_area[i][j]][size]
            fishing_area[i][j] = 0
            break
    shark_check = 0
    fishing_area_after_move = [[0] * (C) for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if fishing_area[y][x] == 0:
                continue
            move_shark(x, y)
    fishing_area = fishing_area_after_move
print(total_catched)