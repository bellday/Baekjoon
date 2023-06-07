from collections import deque
def solution(A, B):
    answer = 0; i=0
    A = sorted(A,reverse = True)
    B = sorted(B, reverse = True)
    queue = deque(B)
    while queue:
        if queue[0]> A[i]:
            queue.popleft()
            answer+=1
        else:
            queue.pop()
        i+=1
            
    return answer