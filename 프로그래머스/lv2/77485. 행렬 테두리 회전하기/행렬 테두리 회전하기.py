def solution(rows, columns, queries):
    answer = []
    graph=[[0]* columns for _ in range(rows)]
    num=1
    d=0
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    #그래프 설정
    for i in range(rows):
        for j in range(columns):
            graph[i][j]=num
            num+=1
            
    # 행렬 회전 설정
    # x세로, y가로
    for q in queries:
        x=q[0]-1
        y=q[1]-1
        x1=q[0]-1
        y1=q[1]-1
        x2=q[2]-1
        y2=q[3]-1
        #시작점 설정
        temp=[graph[x][y]]
        total =2*((x2-x1)+ (y2-y1))
        for c in range(total):
            
            nx=x + dx[d]
            ny = y + dy[d]
            #범위를 벗어난 경우 재정의
            if nx<x1 or nx >x2 or ny <y1 or ny > y2:
                d=(d+1)%4
                nx=x + dx[d]
                ny = y + dy[d]
            temp.append(graph[nx][ny])
            #nx ny를 추가했기 때문에 이전의 값인 len -2 로 구현
            graph[nx][ny]= temp[len(temp)-2]
            x=nx
            y=ny
        answer.append(min(temp))
    
    return answer