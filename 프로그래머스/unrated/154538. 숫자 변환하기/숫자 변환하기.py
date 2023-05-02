from collections import deque
def solution(x, y, n):
    answer = -1
    num_dict={}
    cnt=0
    queue = deque([(x,cnt)])
    while queue:
        
        num_x,c=queue.popleft()
        
        if num_x == y:
            answer=c
            break
        next_x= num_x+n
        if next_x <=y:
            if next_x not in num_dict:
                queue.append((next_x,c+1))
                num_dict[next_x]=c
        next_x= 2*num_x
        if next_x <=y:
            if next_x not in num_dict:
                queue.append((next_x,c+1))
                num_dict[next_x]=c
        next_x= 3*num_x
        if next_x <=y:
            if next_x not in num_dict:
                queue.append((next_x,c+1))
                num_dict[next_x]=c 
        
    return answer