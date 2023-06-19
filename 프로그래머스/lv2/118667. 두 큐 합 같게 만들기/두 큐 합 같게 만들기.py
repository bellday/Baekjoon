# popleft , append 하기. 만약 합이 작다면 다른곳에서 가져오기로 구현
from collections import deque
def solution(queue1, queue2):
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    SameAmountQueue = (sum_q1 + sum_q2)//2
    cnt = 0
    if (sum_q1 + sum_q2) %2 ==1:
        return -1
    Queue1 = deque(queue1)
    Queue2 = deque(queue2)
    answer = -1
    
    while True:
        #같으면 빠져나오기
        if sum_q1 ==sum_q2:
            answer = cnt
            break
        #길이의 2배만큼 돌았지만 못했을 경우 빠져나오기
        if cnt >= len(queue1)*3:
            break
        #클 경우 popleft  
        if sum_q1 > SameAmountQueue:
            num = Queue1.popleft()
            sum_q1-=num
            sum_q2+=num
            Queue2.append(num)
            cnt+=1
        #작을 경우 Queue2 에서 가져온다
        else:
            num = Queue2.popleft()
            sum_q2-=num
            sum_q1+=num
            Queue1.append(num)
            cnt+=1
    return answer