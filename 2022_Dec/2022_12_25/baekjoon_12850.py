# https://www.acmicpc.net/problem/12850

def mutiply(m1, m2):
    result_matrix = [[0] * BUILDING_NUM for _ in range(BUILDING_NUM)]
    for i in range(BUILDING_NUM):
        for j in range(BUILDING_NUM):
            total_sum = 0
            for k in range(BUILDING_NUM):
                total_sum += m1[i][k] * m2[k][j]
            result_matrix[i][j] = total_sum % 1000000007
    return result_matrix
BUILDING_NUM = 8
campus = [[0, 1, 1, 0, 0, 0, 0, 0], 
[1, 0, 1, 1, 0, 0, 0, 0],
[1, 1, 0, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 0, 1, 0]]

cases = [[1 if i == j else 0 for i in range(BUILDING_NUM)] for j in range(BUILDING_NUM)]

D = int(input())

while D:
    if D % 2:
        cases = mutiply(cases, campus)
        D-=1
    campus = mutiply(campus, campus)
    D /= 2
print(cases[0][0])