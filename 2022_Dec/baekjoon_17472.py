# https://www.acmicpc.net/problem/17472

def dfs(x, y, island_num):
    if visited[y][x] or not country_map[y][x]:
        return
    visited[y][x] = 1
    country_map[y][x] = island_num
    islands[island_num].append((x,y))
    if 0 <= x-1 < M:
        dfs(x-1, y, island_num)
    if 0 <= x+1 < M:
        dfs(x+1, y, island_num)
    if 0 <= y-1 < N:
        dfs(x, y-1, island_num)
    if 0 <= y+1 < N:
        dfs(x, y+1, island_num)
def explore_bridge(x, y):
    x_, y_ = x, y
    while x_+1 < M:
        x_ += 1
        if country_map[y_][x_]:
            if x_ - x > 2 and country_map[y_][x_] != country_map[y][x]:
                bridges.append((x_ - x - 1, country_map[y][x], country_map[y_][x_]))
            break
    x_, y_ = x, y
    while x_-1 >= 0:
        x_ -= 1
        if country_map[y_][x_]:
            if x - x_ > 2 and country_map[y_][x_] != country_map[y][x]:
                bridges.append((x - x_ - 1, country_map[y][x], country_map[y_][x_]))
            break
    x_, y_ = x, y
    while y_+1 < N:
        y_ += 1
        if country_map[y_][x_]:
            if y_ - y > 2 and country_map[y_][x_] != country_map[y][x]:
                bridges.append((y_ - y - 1, country_map[y][x], country_map[y_][x_]))
            break
    x_, y_ = x, y
    while y_-1 >= 0:
        y_ -= 1
        if country_map[y_][x_]:
            if y - y_ > 2 and country_map[y_][x_] != country_map[y][x]:
                bridges.append((y - y_ - 1, country_map[y][x], country_map[y_][x_]))
            break
def find(a):
    if parent[a] < 0:
        return a
    else:
        ancestor = find(parent[a])
        parent[a] = ancestor
        return ancestor
def union(a, b):
    a = find(a)
    b = find(b)
    if a==b:
        return True, parent[a]
    if parent[a] > parent[b]:
        a, b = b, a
    parent[a] += parent[b]
    parent[b] = a
    return False, parent[a]
    
N, M = map(int, input().split())
country_map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
islands = [None]

island_num = 0
for y in range(N):
    for x in range(M):
        if country_map[y][x] and not visited[y][x]:
            islands.append([])
            island_num+=1
            dfs(x, y, island_num)



bridges = []
for i in range(1, island_num):
    for x, y in islands[i]:
        explore_bridge(x, y)

bridges.sort()
min_cost = 0
parent = [-1] * (island_num+1)
child_num = 0
for cost, a, b in bridges:
    is_union, child_num = union(a, b)
    if is_union:
        continue
    min_cost += cost
    if -child_num == island_num:
        break
print(min_cost if -child_num == island_num else -1)