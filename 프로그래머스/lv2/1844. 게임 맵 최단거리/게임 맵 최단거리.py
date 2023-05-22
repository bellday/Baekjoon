from collections import deque
def solution(maps):
    answer = 0
    h = len(maps)
    w=len(maps[0])
    visited=[[False]* w for _ in range(h)]
    queue= deque([(0,0,1)])
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    
    while queue:
        
        x,y,d= queue.popleft()

        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if 0<= nx<h and 0<= ny < w and maps[nx][ny]==1 and visited[nx][ny]==False:
                if nx==h-1 and ny ==w-1:
                    return d+1
                visited[nx][ny]=True
                queue.append((nx,ny,d+1))
        
    return -1