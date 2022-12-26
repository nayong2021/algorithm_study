# https://www.acmicpc.net/problem/2098

import sys
INF = sys.maxsize

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1<<N) for _ in range(N)]
END = (1 << N) - 1

def TSP(cur, visited):
    if visited == END:
        return costs[cur][0] if costs[cur][0] != 0 else INF
    if dp[cur][visited]:
        return dp[cur][visited]
    dp[cur][visited] = INF
    for i in range(N):
        if costs[cur][i] == 0:
            continue
        if visited & (1 << i):
            continue
        dp[cur][visited] = min(dp[cur][visited], costs[cur][i] + TSP(i, visited | 1 << i))
    return dp[cur][visited]

print(TSP(0, 1))