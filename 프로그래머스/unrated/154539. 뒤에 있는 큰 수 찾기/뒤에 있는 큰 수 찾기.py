def solution(numbers):
    answer = [0] * len(numbers)
    stack=[]
    for n in range(len(numbers)):
        
        while len(stack) >0 and numbers[stack[-1]] < numbers[n]:
            answer[stack.pop()]=numbers[n]
        stack.append(n)
    while stack:
        answer[stack.pop()] = -1
    return answer