# 최댓값을 계속 줄여나가야함
#최댓값 구하는 방법 => heap
import heapq
def solution(n, works):
    answer = 0
    OvertimeList=[]
    for i in works:
        heapq.heappush(OvertimeList,-i)
    
    for j in range(n):
        number = heapq.heappop(OvertimeList)
        if number != 0:
            number+=1
        heapq.heappush(OvertimeList,number)
    for k in OvertimeList:
        answer += k*k
        
    return answer