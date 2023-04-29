# 아래 오른쪽 위 
def solution(n):
    x=0;y=0;i=0
    #남 동 북서
    dx=[1,0,-1]
    dy=[0,1,-1]
    graph=[[0]*n for _ in range(n)]
    answer = []
    max_num=((n+1)*n)//2
    num=1
    while True:
        
        if num==max_num+1:
            break
        else:
            graph[x][y]=num
            num+=1
            
            nx=x+dx[i]
            ny=y+dy[i]
            #nx,ny가 2차원 배열을 out하는 경우 방향 전환
            if 0>nx or nx>=n or 0>ny or ny>=n or graph[nx][ny] != 0:
                i=(i+1)%3
                nx=x+dx[i]
                ny=y+dy[i]
            x=nx
            y=ny
    for i in range(n):
        for j in range(n):
            if graph[i][j]>0:
                answer.append(graph[i][j])
    
    return answer