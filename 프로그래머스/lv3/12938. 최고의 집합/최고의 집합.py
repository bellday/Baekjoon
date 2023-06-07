#s의 값이 n보다 작을 경우 -> 자연수 1로 배정을 못하는 경우
#n의 최댓값으로 해도 s값을 구현못하는 경우 -> 최고의 집합 구현 못함
def solution(n, s):
    answer = []


    num = s // n
    left = s % n
    if num ==0:
        return [-1]
    
    answer = [num] * n
    for i in range(left):
        answer[i] += 1
    return sorted(answer)