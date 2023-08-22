def solution(num_list):
    answer = 1
    if len(num_list)>= 11:
        answer = sum(num_list)
    else:
        for i in num_list:
            answer *= i
    return answer