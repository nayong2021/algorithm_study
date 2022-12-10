# https://www.acmicpc.net/problem/17299

N = int(input())
A = list(map(int, input().split()))
F = {}
NGF = [-1] * N
for i in A:
    F[i] = F.get(i, 0)
    F[i] += 1
stack = []
for i in range(N):
    while stack:
        if F[A[stack[-1]]] < F[A[i]]:
            fewer_than_i = stack.pop()
            NGF[fewer_than_i] = A[i]
        else:
            break
    stack.append(i)
for i in NGF:
    print(i, end = ' ')