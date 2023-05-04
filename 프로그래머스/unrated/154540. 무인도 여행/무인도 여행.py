from collections import deque
def solution(maps):
    answer = []
    width = len(maps[0])
    heigh = len(maps)
    visited= [[0]* width for _ in range(heigh)]
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(heigh):
        for j in range(width):
            if maps[i][j].isdigit()  == True and visited[i][j] == 0:
                queue = deque([(i,j)])
                area=0
                while queue:
                    x, y = queue.popleft()
                    visited[x][y]=1
                    area=  area +int(maps[x][y])
                    for d in range(4):
                        
                        nx = x + dx[d]
                        ny = y + dy[d]
                        
                        if 0<= nx < heigh and 0<= ny < width:
                            if visited[nx][ny]==0 and maps[nx][ny].isdigit()== True:
                                queue.append((nx,ny))
                                visited[nx][ny]=1
                
                answer.append(area)
            
    
    
    
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        answer.sort()
    return answer

