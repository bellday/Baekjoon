from collections import deque
def solution(board):
    answer = 0
    height = len(board)
    width = len(board[0])
    visited = [[0]* width for _ in range(height)]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    for i in range(height):
        for j in range(width):
            if board[i][j]=='R':
                q = deque([(i,j,answer)])
                visited[i][j]=1
                while q:
                    
                    x,y,d = q.popleft()
                    tmpx=x
                    tmpy=y
                    if board[x][y]=='G':
                        answer = d
                        break
                    for k in range(4):
                        x=tmpx
                        y=tmpy
                        while True:
                            
                            
                            nx = x+dx[k]
                            ny = y+dy[k]
                            if nx ==height or ny ==width or nx ==-1 or ny ==-1:
                                break
                            elif board[nx][ny]=='D':

                                break
                            x=nx
                            y=ny
                        
                        if visited[x][y]==0:
                            visited[x][y]=1
                            q.append((x,y,d+1))
                            #print(x,y,d)
    if answer==0:
        return -1
    return answer