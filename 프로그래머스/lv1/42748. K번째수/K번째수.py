def solution(array, commands):
    result=[]
    for num in range(len(commands)):
        k= commands[num][2]
        answer = array[commands[num][0]-1:commands[num][1]]
        answer.sort()
        result.append(answer[k-1])
        
    return result