def solution(num_list):
    answer_sum = sum(num_list)
    answer_mul = 1
    for i in num_list:
        answer_mul *= i
    return 1 if answer_mul < answer_sum**2 else 0