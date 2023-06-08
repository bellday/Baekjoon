#제일 앞의것을 꺼내와야함 큐를 사용
#꺼낸값을 for 문을 돌려서 확인 만약 큰 값이 있으면 cnt +1 하고 break 이후 스택에 추가
# 아닐경우 j를 인쇄
#만약 앞에있는것이 출력되면 -1 아니면 그냥
#내가 찾는 값이 이동하는 경우 len(queue)-1 로변경
from collections import deque
def solution(priorities, location):
    answer = 1
    queue=deque(priorities)
    num=-1
    while queue:
        j= queue.popleft()
        num+=1
        
        for i in queue:#추가여부 만약 j의 우선순위가 높다면 빠져나감
            if j<i:
                queue.append(j)
                j=-1  # 이동여부를 표시하기 위해
                if num == location:# 만약 num 과 location 이 같다면
                    location = len(queue)
                    num=0
                
                break
        
        if j >-1: #-1 이 아니라면 출력을 알리기 위함
            
            if num == location:
                
                return answer
            else:
                answer+=1
    
    
    