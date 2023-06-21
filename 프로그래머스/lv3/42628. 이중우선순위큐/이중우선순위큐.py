'''
최대 최소값은 힙 자료구조가 가장 효율적임.
힙 자료구조 사용
최대힙과 최소힙을 사용하여 구현한다. 최댓값은 push할 때 -1을 곱해서 구현한다.
힙에 자료가있을 때만 작동하도록 구현
마지막에 힙에 자료가 없으면 [0,0] 리턴 아닐경우 최댓값 최솟값 리턴
'''
import heapq
def solution(operations):
    answer = []
    max_heap = []
    min_heap =[]
    for o in operations:
        #I 일 경우 최솟값 힙, 최댓값 힙에 삽입
        if o[:1] == 'I':
            heapq.heappush(min_heap,int(o[1:]))
            heapq.heappush(max_heap,-int(o[1:]))
        else:
            # D일 경우 최솟값 힙, 최댓값 힙 삭제
            if o[2:] == '-1': # 최솟값 삭제 
                
                if min_heap:
                    num = heapq.heappop(min_heap)
                    max_heap.remove( -1* num)
            else:
                if min_heap:
                    num = heapq.heappop(max_heap)
                    min_heap.remove(-1*num)
            
    if min_heap:
        return [-1 * heapq.heappop(max_heap) ,heapq.heappop(min_heap) ]
    else:
        return [0,0]
    