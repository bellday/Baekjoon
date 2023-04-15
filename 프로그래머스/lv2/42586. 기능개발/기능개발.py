#앞의 기능이 먼저 100%되면 빠져나감
#배포마다 몇개의 기능이 배포되는지 출력하기
#배포는 하루에 한번
from collections import deque
def solution(progresses, speeds):
    answer = []
    progress_list=[]
    cnt=0
    for pro in progresses:
        progress_list.append(100-pro)
    #print(progress_list)
    for i in range(len(progress_list)):
        if progress_list[i]%speeds[i]==0:
            progress_list[i]=progress_list[i]//speeds[i]
        else:
            progress_list[i]=progress_list[i]//speeds[i]+1
    #print(progress_list)
    queue=deque(progress_list)
    print(queue)
    while queue:
        
        if len(queue)==0:
            break
        
        days=queue.popleft()
        cnt+=1
        while queue:
            if days<queue[0]:
                answer.append(cnt)
                cnt=0
                break
            else:
                queue.popleft()
                cnt+=1
        
    answer.append(cnt)
    return answer