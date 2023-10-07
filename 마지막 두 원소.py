def solution(num_list):
    answer = [0 for i in range(len(num_list)+1)]
    for i in range(len(num_list)):
        answer[i] = num_list[i]
    if num_list[-1] > num_list[-2]:
        answer[-1] = num_list[-1] - num_list[-2]
    else:
        answer[-1] = num_list[-1]*2
    return answer