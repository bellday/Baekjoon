def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[len(numbers)-1])
        for j in range(len(numbers)-1):
            answer.append(numbers[j])
        return answer
    else:
        for a in range(1,len(numbers)):
            answer.append(numbers[a])
        answer.append(numbers[0])
        return answer