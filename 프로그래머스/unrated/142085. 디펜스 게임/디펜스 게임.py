import heapq
def solution(n, k, enemy):
    
    answer = 0
    heap=[]
    heapq.heapify(heap)
    for e in enemy:
        heapq.heappush(heap,-e)
        if n<e and  k==0:
            break
        if n>=e:
            n-=e
            answer+=1
        else:
            if heap and k>0 :
                k-=1
                num= heapq.heappop(heap)
                n+= -num
                n-=e
                answer+=1
        
            
    return answer