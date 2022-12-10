# https://www.acmicpc.net/problem/2629

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
to_validates = list(map(int, input().split()))

can_validates = {}

for weight in weights:
    temp = can_validates.copy()
    for can_validate in temp:
        can_validates[can_validate + weight] = 1
        can_validates[can_validate - weight] = 1
    can_validates[weight] = 1
    can_validates[-weight] = 1
for to_validate in to_validates:
    print('Y' if to_validate in can_validates else 'N', end = ' ')