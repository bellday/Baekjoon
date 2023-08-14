def solution(numbers):
    
    answer = sorted(numbers)
    return answer[len(numbers)-1]*answer[len(numbers)-2]