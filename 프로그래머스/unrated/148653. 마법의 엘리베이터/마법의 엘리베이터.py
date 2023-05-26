def solution(storey):
    answer = 0
    
    while storey:
        num1 = storey %10
        num10 =(storey /10) %10
        if num1 >5:
            answer += 10 - num1
            storey+=10
        elif num1 ==5:
            if num10 >=5:
                storey+=10
                answer+= 10 - num1
            else:
                storey+=0
                answer+= num1
        else:
            answer+= num1
        storey = storey//10
    return answer