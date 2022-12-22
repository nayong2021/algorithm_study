# https://www.acmicpc.net/problem/9252

A = input()
B = input()
dp = [''] * len(B)
for a in A:
    lcs = ''
    for i, b in enumerate(B):
        if a == b and len(dp[i]) <= len(lcs):
            dp[i] = lcs + a
        elif len(dp[i]) > len(lcs):
            lcs = dp[i]
LCS = max(dp, key=lambda x:len(x))
print(len(LCS))
if len(LCS):
    print(LCS)