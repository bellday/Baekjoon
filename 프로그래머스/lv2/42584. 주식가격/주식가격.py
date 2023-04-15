from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        cnt=0
        price = queue.popleft()
        for i in queue:
            if price<=i:
                cnt+=1
            if price>i:
                cnt+=1
                break
        answer.append(cnt)
    
    return answer