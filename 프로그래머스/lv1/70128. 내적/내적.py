def solution(a, b):
    answer =0
    i = 0
    for num in range(len(a)):
        answer+= a[i]*b[i]
        i+=1
    return answer