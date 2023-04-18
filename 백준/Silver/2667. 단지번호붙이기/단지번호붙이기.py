# n개의 정사각형
# 배열 구성
# 처음부터 1을 찾기 찾으면  dfs 돌리기
# dfs 정지조건 : 다찾았을 때 없으면 pass
# 갯수 부분양 카운트

n= int(input())
graph=[list(map(int,input())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
#동 남 서 북
dx=[0,1,0,-1]
dy=[1,0,-1,0]
cnt=0
amount_list=[]
amt=0
def dfs(x,y):
    global  amt
    visited[x][y]=True
    amt+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<= nx < n and 0<= ny < n and graph[nx][ny]==1 and visited[nx][ny]==False:
            dfs(nx,ny)



for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==False:
            amt=0
            cnt+=1
            dfs(i,j)
            amount_list.append(amt)
print(cnt)
amount_list.sort()
for a in amount_list:
    print(a)
