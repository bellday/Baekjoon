from collections import deque
def solution(places):
    answer = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for place in places:
        cnt=0
        visited=[[0]*5 for _ in range(5)]
        
        for i in range(5):
            
            for j in range(5):
                
                if place[i][j]=='P':
                    visited[i][j]=1
                    d=0
                    queue = deque([(i,j,d)])
                    
                    while queue:
                        
                        x,y,d= queue.popleft()
                        if place[x][y] =='P' and d<=2 and d>=1:
                            cnt+=1
                            break
                        for z in range(4):
                            nx = x+dx[z]
                            ny = y + dy[z]
                            if 0<= nx<5 and 0<= ny <5:
                                if visited[nx][ny] ==0 and place[nx][ny] !='X' and d<2:
                                    queue.append((nx,ny,d+1))
        if cnt ==0:
            answer.append(1)
        else:
            answer.append(0)
        
    
    return answer