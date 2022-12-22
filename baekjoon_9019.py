# https://www.acmicpc.net/problem/9019
from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

def get_ds(n):
    d1 = int(n / 1000)
    n -= d1 * 1000
    d2 = int(n / 100)
    n -= d2 * 100
    d3 = int(n / 10)
    n -= d3 * 10
    d4 = n
    return d1, d2, d3, d4

def D(n):
    return 2 * n % 10000, 'D'

def S(n):
    return (n + 9999) % 10000, 'S'

def L(n):
    d1, d2, d3, d4 = get_ds(n)
    return 1000 * d2 + 100 * d3 + 10 * d4 + d1, 'L'

def R(n):
    d1, d2, d3, d4 = get_ds(n)
    return 1000 * d4 + 100 * d1 + 10 * d2 + d3, 'R'

for _ in range(T):
    A, B = map(int, input().split())
    commands = [0] * 10000
    commands[A] = ''
    queue = deque([A])
    while True:
        current = queue.popleft()
        if current == B:
            break
        for i, command in (D(current), S(current), L(current), R(current)):
            if commands[i] == 0:
                commands[i] = commands[current] + command
                queue.append(i)
    print(commands[B])
    