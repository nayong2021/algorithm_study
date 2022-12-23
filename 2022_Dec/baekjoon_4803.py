# https://www.acmicpc.net/problem/4803

import sys
input=sys.stdin.readline

test_num = 1

def dfs(node, parent):
    visited[node] = True
    for child in graph[node]:
        if child == parent:
            continue
        if visited[child]:
            return False
        if not dfs(child, node):
            return False
    return True
        
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n+1)
    T = 0
    for i in range(1, n+1):
        if not visited[i] and dfs(i, None):
            T+=1
    print('Case {}:'.format(test_num), end=' ')
    if T==0:
        print('No trees.')
    elif T==1:
        print('There is one tree.')
    else:
        print('A forest of', T, 'trees.')
    test_num+=1