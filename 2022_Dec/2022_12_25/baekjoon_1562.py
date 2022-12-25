# https://www.acmicpc.net/problem/1562

N = int(input())
stair_nums = [{} for _ in range(10)]
for i in range(1, 10):
    stair_nums[i][tuple(1 if i == j else 0 for j in range(10))] = 1
condition_satisfied_stair_nums = [0] * 10

for n in range(N-1):
    stair_nums_with_n_length = [{} for _ in range(10)]
    condition_satisfied_stair_nums_with_n_length = [0] * 10
    for i in range(10):
        for stair_num in stair_nums[i]:
            if i-1 >= 0:
                temp = list(stair_num)
                temp[i-1] = 1
                if sum(temp) == 10:
                    condition_satisfied_stair_nums_with_n_length[i-1] += stair_nums[i][stair_num]
                else:
                    stair_nums_with_n_length[i-1][tuple(temp)] = stair_nums_with_n_length[i-1].get(tuple(temp), 0) + stair_nums[i][stair_num]
            if i+1 < 10:
                temp = list(stair_num)
                temp[i+1] = 1
                if sum(temp) == 10:
                    condition_satisfied_stair_nums_with_n_length[i+1] += stair_nums[i][stair_num]
                else:
                    stair_nums_with_n_length[i+1][tuple(temp)] = stair_nums_with_n_length[i+1].get(tuple(temp), 0) + stair_nums[i][stair_num]
        if i-1 >= 0:
            condition_satisfied_stair_nums_with_n_length[i-1] += condition_satisfied_stair_nums[i]
        if i+1 < 10:
            condition_satisfied_stair_nums_with_n_length[i+1] += condition_satisfied_stair_nums[i]
    stair_nums = stair_nums_with_n_length
    condition_satisfied_stair_nums = [i for i in condition_satisfied_stair_nums_with_n_length]
print(sum(condition_satisfied_stair_nums) % 1000000000)