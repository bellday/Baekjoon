def solution(num_list):
    answer = []
    a=0
    b=0
    for num in range(len(num_list)):
        if num_list[num]%2 ==0:
            a=a+1
        else:
            b=b+1
    answer.append(a)
    answer.append(b)
    return answer