def solution(n):
    times = n//2
    odd_case= n%2
    answer =times*'수박'+odd_case*'수'
    return answer