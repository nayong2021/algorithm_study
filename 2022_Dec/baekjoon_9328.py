# https://www.acmicpc.net/problem/9328

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

def explore_building(x, y):
    global doc_founded
    cur = building_map[y][x]
    if cur == '*':
        return
    if visited[y][x]:
        return
    if 'a' <= cur <= 'z' and not keys.get(cur, 0):
        keys[cur] = 1
        for x_, y_ in door_founded.get(cur[:].upper(), []):
            explore_building(x_, y_)
    if 'A' <= cur <= 'Z' and not keys.get(cur[:].lower(), 0):
        door_founded[cur] = door_founded.get(cur, [])
        door_founded[cur].append((x, y))
        return
    if cur == '$':
        doc_founded += 1
    visited[y][x] = 1
    if 0 <= x-1:
        explore_building(x-1, y)
    if x+1 < w:
        explore_building(x+1, y)
    if 0 <= y-1:
        explore_building(x, y-1)
    if y+1 < h:
        explore_building(x, y+1)
    

for _ in range(T):
    h, w = map(int, input().split())
    building_map = [list(input().strip()) for _ in range(h)]
    keys = {key : 1 for key in list(input().strip())}
    visited = [[0] * w for _ in range(h)]
    door_founded = {}
    doc_founded = 0
    for i in range(h):
        explore_building(0, i)
        explore_building(w-1, i)
    for i in range(w):
        explore_building(i, 0)
        explore_building(i, h-1)
    print(doc_founded)
    