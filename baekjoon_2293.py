# https://www.acmicpc.net/problem/2293

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)

cases = [0] * (k+1)
cases[0] = 1
for coin in coins:
    for i in range(k+1):
        if i - coin >= 0:
            cases[i] += cases[i-coin]
print(cases[k])