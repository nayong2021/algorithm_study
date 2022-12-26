import sys
INF = sys.maxsize

costs = [[1, 2, 2, 2, 2],
[2, 1, 3, 4, 3],
[2, 3, 1, 3, 4],
[2, 4, 3, 1, 3],
[2, 3, 4, 3, 1]]

sequences = list(map(int, input().split()))
sequences.pop()
cases = {(0, 0) : 0}

for i in sequences:
    next_cases = {}
    for case in cases:
        l, r = case
        next_cases[(i, r)] = min(next_cases.get((i, r), INF), cases[case] + costs[l][i])
        next_cases[(l, i)] = min(next_cases.get((l, i), INF), cases[case] + costs[r][i])
    cases = next_cases
print(min(cases.values()))