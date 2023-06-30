import heapq

def solution(n, edge):
    answer = 0
    maximum_depth = 0
    visit = [False] *(n+1)
    graph = [[] for _ in range(n+1)]
    dist_arr = [100000000] * (n+1)
    dist_arr[1] =0
    for e0,e1 in edge:
        graph[e0].append(e1)
        graph[e1].append(e0)
    heap = []
    #거리 , 노드
    heapq.heappush(heap,[0,1])
    
    while heap:
        
        dist, node = heapq.heappop(heap)
        visit[node] = True
        if maximum_depth < dist:
            maximum_depth = dist
        if dist_arr[node] > dist+1:
            dist_arr[node] = dist+1
        for i in graph[node]:
            
            if visit[i] == False:
                visit[i] = True
                heapq.heappush(heap,[dist+1,i])
    maximum_depth = max(dist_arr[1:])
    
    
    return dist_arr.count(maximum_depth)