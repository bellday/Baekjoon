#bfs 로 돌리기
#bfs 횟수는 4-> 7, 5-> 15 2 ^n-1 -1
#횟수가 돌면 멈추기
#더하는 값은 2 -> 4 -> 8 이렇게 증가하도록 구현
from collections import deque
def solution(numbers, target):
    answer = 0
    queue=deque([(0)])
    cnt=2*((2**(len(numbers)-1))-1)
    count=0
    add_cnt=1
    check =0
    i=0
    
    while count != cnt:
        count+=1
        num=queue.popleft()
        if check == add_cnt:
            add_cnt*=2
            check=1
            i+=1
            queue.append(num + numbers[i])
            queue.append(num - numbers[i])
        else:
            check+=1
            queue.append(num + numbers[i])
            queue.append(num - numbers[i])
    answer=queue.count(target)
    return answer