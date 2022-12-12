#https://www.acmicpc.net/problem/11401

p = 1000000007

N, K = map(int, input().split())

result = 1

for i in range(N-K+1, N+1):
    result = (result * i) % p

k_factorial = 1

for i in range(1, K+1):
    k_factorial = (k_factorial * i) % p

def pow(a, n, p):
    if n == 1:
        return a
    if n % 2 == 0:
        return pow((a*a)%p, int(n/2), p)
    if n % 2 == 1:
        return (pow((a*a)%p, int(n/2), p) * a) % p

result = (result * pow(k_factorial, p-2, p)) % p

print(result)