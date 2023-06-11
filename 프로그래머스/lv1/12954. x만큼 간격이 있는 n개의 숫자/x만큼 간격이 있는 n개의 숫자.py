def solution(x, n):
    answer = []
    add_num = 0
    for i in range(n):
        add_num+=x
        answer.append(add_num)
    return answer