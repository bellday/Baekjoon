n,m,x,y,d=map(int,input().split())#x=세로 #y는 가로
graph=[list(map(int,input().split())) for _ in range(n)]

dir=list(map(int,input().split())) #방향
dice={'2':0,'4':0,'1':0,'3':0,'5':0,'6':0}

dy=[1,-1,0,0]
dx=[0,0,-1,1]

for j in dir:
    if j==1: #동
        nx=x+dx[0]
        ny=y+dy[0]
        if 0 <= nx < n and 0 <= ny < m:
            dice['4'],dice['1'],dice['3'],dice['6']=dice['6'],dice['4'],dice['1'],dice['3']

            if graph[nx][ny]==0:
                graph[nx][ny]=dice['6']
            else:
                dice['6'] = graph[nx][ny]
                graph[nx][ny]=0
            x=nx
            y=ny
            print(dice['1'])
    elif j==2: #서
        nx=x+dx[1]
        ny=y+dy[1]
        if 0 <= nx < n and 0 <= ny < m:
            dice['4'], dice['1'], dice['3'], dice['6'] =dice['1'],dice['3'],dice['6'],dice['4']

            if graph[nx][ny]==0:
                graph[nx][ny]=dice['6']
            else:
                dice['6'] = graph[nx][ny]
                graph[nx][ny]=0
            x=nx
            y=ny
            print(dice['1'])
    elif j==3: #북
        nx=x+dx[2]
        ny=y+dy[2]
        if 0 <= nx < n and 0 <= ny < m:
            dice['2'],dice['1'],dice['5'],dice['6']=dice['1'],dice['5'],dice['6'],dice['2']

            if graph[nx][ny]==0:
                graph[nx][ny]=dice['6']
            else:
                dice['6'] = graph[nx][ny]
                graph[nx][ny]=0
            x=nx
            y=ny
            print(dice['1'])
    elif j==4: #남
        nx=x+dx[3]
        ny=y+dy[3]
        if 0 <= nx < n and 0 <= ny < m:
            dice['2'],dice['1'],dice['5'],dice['6']=dice['6'],dice['2'],dice['1'],dice['5']

            if graph[nx][ny]==0:
                graph[nx][ny]=dice['6']
            else:
                dice['6'] = graph[nx][ny]
                graph[nx][ny]=0
            x=nx
            y=ny
            print(dice['1'])




