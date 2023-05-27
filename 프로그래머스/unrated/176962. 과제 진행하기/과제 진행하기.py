#과제 -> 스택으로 접근한다.
# 시작 종료 시간

def solution(plans):
    answer = []
    __plans=sorted(plans,key=lambda x: x[1])
    print(__plans)
    process= []
    for s in range(len(__plans)-1):
        start = int(__plans[s][1][:2]) *60 + int(__plans[s][1][3:])
        start2= int(__plans[s+1][1][:2]) *60 + int(__plans[s+1][1][3:])
        end = start + int(__plans[s][2])
        
        between_time = start2 - end
        
        # 끝나는 시간이 더 클 경우
        if end > start2:
            process.append([__plans[s][0],end-start2])
            
        else:
        #아니면 숙제 끝
            answer.append(__plans[s][0])
            if process:
                while True:
                    if len(process)==0 or between_time ==0:
                        break
                    if between_time >=process[-1][1]:
                        answer.append(process[-1][0])
                        #print(process[-1][0], between_time, process[-1][1])
                        between_time-= process[-1][1]
                        process.pop()
                    else:
                        temp = process[-1][1]
                        process[-1][1] = temp - between_time
                        between_time =0
    
        
    answer.append(__plans[-1][0])
    while process:
        task, time =process.pop()
        answer.append(task)
    #print(process)     
    #print(start)
    return answer