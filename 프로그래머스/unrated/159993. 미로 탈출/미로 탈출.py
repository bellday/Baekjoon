from collections import deque
def solution(maps):
    answer = 0
    height = len(maps)
    width = len(maps[0])
    visited1=[[0]* width for _ in range(height)]
    visited2=[[0]* width for _ in range(height)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(height):
        for j in range(width):
            if maps[i][j]=='S':
                queue = deque([(i,j,answer)])
                visited1[i][j] =1
                while queue:
                    
                    x,y,d= queue.popleft()
                    if maps[x][y]=='L':
                        answer=d
                        break
                    
                    for k in range(4):
                        nx =x+dx[k]
                        ny =y+dy[k]
                        if 0<=nx< height and 0<= ny < width:
                            if maps[nx][ny] != 'X' and visited1[nx][ny]== 0:
                                visited1[nx][ny]=1
                                queue.append((nx,ny,d+1))
                if answer ==0:
                    return -1
                queue = deque([(x,y,d)])
                print(x,y,d)
                visited2[x][y]=1
                while queue:
                    x,y,d = queue.popleft()
                    if maps[x][y]=='E':
                        answer = d
                        break
                    for k in range(4):
                        nx =x+dx[k]
                        ny =y+dy[k]
                        if 0<=nx< height and 0<= ny < width:
                            if maps[nx][ny] != 'X' and visited2[nx][ny]== 0:
                                visited2[nx][ny]=1
                                queue.append((nx,ny,d+1))
                if answer <d:
                    return -1
    return answer