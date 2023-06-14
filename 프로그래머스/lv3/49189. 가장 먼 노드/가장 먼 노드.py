'''
다익스트라로 풀기
힙 필요
'''
import heapq
def solution(n, edge):
    answer = 0
    Max_distance = 0 # 최대 거리 갯수
    Range = [1000000000] *(n+1) #각 노드의 거리
    NodeGraph = [[] for _ in range(n+1) ]
    
    #그래프 설정
    for e in edge:
        x= e[0] ; y = e[1]
        NodeGraph[y].append(x)
        NodeGraph[x].append(y)
    
    heap = [] #거리 , 노드번호
    heapq.heappush(heap,[0,1])
    Range[1] =0
    while heap:
        
        distance, NodeNum = heapq.heappop(heap)
        if Max_distance < distance:
            Max_distance = distance
        
        
        for key, val in enumerate(NodeGraph[NodeNum]):
            
            if distance +1 < Range[val]:
                heapq.heappush(heap,[distance+1,val])
                
                Range[val] = distance +1
    
    for r in Range:
        if r == Max_distance:
            answer +=1
    return answer