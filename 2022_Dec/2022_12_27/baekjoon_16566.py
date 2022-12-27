# https://www.acmicpc.net/problem/16566

import sys
input=sys.stdin.readline

def find(a):
    if a==parent[a]:
        return a
    else:
        ancestor = find(parent[a])
        parent[a] = ancestor
        return ancestor

def union(a, b):
    # a = find(a)
    # b = find(b)
    parent[b] = a

N, M, K = map(int, input().split())
card_available = [0] * (N+1)
parent = [i for i in range(N+1)]
for i in list(map(int, input().split())):
    card_available[i] = 1
for i in list(map(int, input().split())):
    i = find(i)
    for j in range(i+1, N+1):
        if card_available[j]:
            union(j, i)
            print(j)
            break
        else:
            union(i, j)