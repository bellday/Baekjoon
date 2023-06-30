'''
플로이드 마샬 알고리즘 사용
승자 -> 1로 표시, 패자 -> -1 로 표시
a-> b , b->c 이면 a->c이므로 , a->b, b->c 가 1이면 a->c 는 1로(승리) 표시 , c->a 는 -1로 표시
최종적으로 본인은 승패를 할 수 없으므로 해당 배열의 0의 갯수가 0이면 순위를 매길 수 있다고 판단하여 출력

'''

def solution(n, results):
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)]
    for rst in results:
        graph[rst[0]][rst[1]] = 1 #승리표현
        graph[rst[1]][rst[0]] = -1  # 패배 표현
    
    answer = floyd(graph)
    return answer

def floyd(graph):
    cnt =0
    # 거쳐가는 노드(선수)
    for i in range(len(graph)):
        #시작 노드 (승자)
        for j in range(len(graph)):
            #종료 노드(패자)
            for k in range(len(graph)):
                
                if graph[j][i] ==1 and  graph [i][k]==1 : # j가 i를 이기고 i가 k를 이기면
                    graph[j][k] = 1# j가 k를 이기고
                    graph[k][j]=-1 # k가 j에게 진다
    
    for g in graph:
        if g[1:].count(0) ==1: # 0의 수가 1개일 경우 == 자기 자신에 대한 정보만 없을 경우
            cnt+=1
    return cnt