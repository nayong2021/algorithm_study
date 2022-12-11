import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [0] * (10000+1)
dp_next = dp[:]

for i in range(N):
    memory, cost = memories[i], costs[i]
    for c in range(cost, 10000+1):
        dp_next[c] = max(dp[c-cost] + memory, dp[c])
    dp = dp_next[:]
for i in range(10000+1):
    if dp[i] >= M:
        print(i)
        break