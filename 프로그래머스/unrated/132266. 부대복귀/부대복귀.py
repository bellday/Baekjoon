import heapq
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    # 간선 추가
    for start,end in roads:
        graph[start].append(end)
        graph[end].append(start)
    
    dist = [1000000000] *(n+1)
    dist[0]= 0; dist[destination] = 0
    heap = []
    heapq.heappush(heap,(0,destination))
    while heap:
        
        distance, vertex = heapq.heappop(heap)
        
        for i in graph[vertex]:
            
            if dist[i]> distance+1:
                dist[i] = distance+1
                heapq.heappush(heap,(distance+1,i))
    for source in sources:
        
        if dist[source] == 1000000000:
            answer.append(-1)
        else:
            answer.append(dist[source])
        
    return answer