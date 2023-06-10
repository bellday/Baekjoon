# 가장 왼쪽은 왼쪽값만 더한다. 나머지는 좌우의 값을 더한값을 비교하여 max값을 넣는다.
def solution(triangle):
    graph = [[0]* len(triangle) for _ in range(len(triangle)) ]
    answer = 0
    for key , tri in enumerate(triangle):
        for k , i in enumerate(tri):
            
            if k ==0:
                
                graph[key][k] += graph[key-1][k] +int(i)
            else:
                graph[key][k] =  max(graph[key-1][k] + i,graph[key-1][k-1] +i)
    
    return max(graph[len(triangle)-1])