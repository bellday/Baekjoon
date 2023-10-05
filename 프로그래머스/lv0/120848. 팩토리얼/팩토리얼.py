def solution(n):
    answer = 1
    fac = 1
    while fac <= n :
        answer += 1
        fac = fac * answer
    answer = answer-1
    
    return answer       