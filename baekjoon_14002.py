# https://www.acmicpc.net/problem/14002

N = int(input())
A = list(map(int, input().split()))

sequences = [()] * N

for i in range(N-1, -1, -1):
    max_len_sequence = ()
    for j in range(i, N):
        if A[j] > A[i] and len(max_len_sequence) < len(sequences[j]):
            max_len_sequence = sequences[j]
    sequences[i] = (A[i], ) + max_len_sequence
    
max_len_sequence = max(sequences, key=lambda x:len(x))

print(len(max_len_sequence))
for i in max_len_sequence:
    print(i, end=' ')