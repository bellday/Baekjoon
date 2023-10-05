def solution(i, j, k):
    answer = ''
    for num in range(i,j+1):
        answer+=str(num)
    return answer.count(str(k))