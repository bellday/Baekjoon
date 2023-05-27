def solution(targets):
    answer = 0
    targets= sorted(targets, key = lambda x: x[1])
    min_num=0
    for i in targets:
        if min_num <=i[0]:
            min_num=i[1]
            answer+=1
    return answer