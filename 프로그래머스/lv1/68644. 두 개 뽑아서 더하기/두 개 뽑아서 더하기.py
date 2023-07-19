def solution(numbers):
    answer = []
    for num in range(len(numbers)):
        for j in range(num+1,len(numbers)):
            if numbers[num]+numbers[j] not in answer:
                answer.append(numbers[num]+numbers[j])
    answer.sort()
            
    return answer