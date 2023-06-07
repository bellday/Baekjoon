import heapq
#다익스트라
def solution(N, road, K):
    answer = 0
    #거리배열설정
    village = [1000000]*(N+1)
    #사용 편하기위함 N+1 사용
    graph = [[] for _ in range(N+1)]
    
    #그래프 설정
    for r in road:
        vill1, vill2, time = r
        #비용 노드번호 추가
        graph[vill1].append((time,vill2))
        graph[vill2].append((time,vill1))
    q=[]
    village[1] = 0
    heapq.heappush(q,(0,1))
    while q:
        dist , now =heapq.heappop(q)
        
        for i in graph[now]:
            cost = dist + i[0]
            if cost < village[i[1]]:
                village[i[1]] =cost
                heapq.heappush(q,(cost,i[1]))
    #print(village)
    for v in village:
        if K>=v:
            answer+=1
    return answer