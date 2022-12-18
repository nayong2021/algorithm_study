#https://www.acmicpc.net/problem/1717

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

union = [-1 for i in range(n+1)]
commands = [input() for i in range(m)]

def find(n):
    if union[n] < 0:
        return n
    else:
        ancestor = find(union[n])
        union[n] = ancestor
        return ancestor

for command in commands:
    op, a, b = map(int, command.split())
    if op==0:
        a = find(a)
        b = find(b)
        if a==b:
            continue
        if union[b] < union[a]:
            a, b = b, a
        union[b] += union[a]
        union[a] = b
    if op==1:
        a = find(a)
        b = find(b)
        print('YES' if a == b else 'NO')