# https://www.acmicpc.net/problem/9935

input_str = input()
bomb = list(input())
bomb_length = len(bomb)
bombed = []
for alphabet in input_str:
    bombed.append(alphabet)
    if len(bombed) >= bomb_length and bomb[-1] == bombed[-1] and bombed[-bomb_length:] == bomb:
        for _ in range(bomb_length):
            bombed.pop()
if bombed:
    print("".join(bombed))
else:
    print("FRULA")