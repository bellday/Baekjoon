from collections import  deque
n, l, r = map(int, input().split())
graph = [0 for _ in range(n)]
day = 0

def bfs():
    dx = [0,1,0,-1]
    dy =[1,0,-1,0]
    move = 0
    width = len(graph)
    visited = [[0]* width for _ in range(width)]
    for i in range(width):
        for j in range(width):
            if visited[i][j]==0:
                visited[i][j]=1
                queue = deque([(i,j)])
                graph_list = [] ;add= 0
                graph_list.append([i,j,graph[i][j]])
                while queue:

                    x,y = queue.popleft()

                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0<= nx <width and 0<= ny <width:
                            if l <= abs(graph[nx][ny] - graph[x][y])  <=r and visited[nx][ny] ==0:
                                visited[nx][ny]=1
                                queue.append((nx,ny))
                                graph_list.append([nx, ny, graph[nx][ny]])

                cnt = len(graph_list)
                if cnt != 1:
                    for c in range(cnt):
                        add += graph_list[c][2]
                    movepeople = add//cnt
                    for c in range(cnt):

                        graph[graph_list[c][0]][graph_list[c][1]] = movepeople
                    move+=1
    #print(graph)
    return move
    #print(l,r)

def printanswer():
    print(day)


for i in range(n):
    graph[i] = list(map(int,input().split()))
while True:
    count = bfs()
    if count ==0:
        break
    day+=1
printanswer()