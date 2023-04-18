from collections import deque
# bfs 사용 
# 상하좌우 토마토가 있으면 값 바꾸기 , 값이 0인경우 바꿔준다.
# 그래프를 순회하며 값이 있을 경우 bfs 시행하지만 큐에 추가 
m,n = map(int,input().split())# m은 상자의 가로 칸, n은 상자의 세로칸

graph=[list(map(int,input().split())) for _ in range(n)]
day=1 # 날짜설정
queue=deque([])
#동남서북 설정
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for i in range(n):
    for j in range(m):
        if graph[i][j]==1: # 익은 경우
            queue.append((i,j))
            
while queue:

    x,y=queue.popleft()

    for d in range(4):
                    
        nx=x+dx[d]
        ny=y+dy[d]
                    
        if 0<=nx < n and 0<= ny < m and graph[nx][ny]==0:#그래프안에있고 방문안했을경우
            queue.append((nx,ny))
            graph[nx][ny]=graph[x][y]+1 # 토마토 익었다고 설정
                                                                        
for i in range(n):
    for j in range(m):
        if graph[i][j]==0: # 만약 안익은 토마토가 있으면
            print(-1)
            exit(0)
        day=max(day,graph[i][j])
print(day-1)