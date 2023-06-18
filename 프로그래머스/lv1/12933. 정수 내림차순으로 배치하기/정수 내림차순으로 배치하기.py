def solution(n):
    list_n = list(str(n))
    list_n.sort(reverse =True)
    answer = ''
    for s in list_n:
        answer+=s
    return int(answer)