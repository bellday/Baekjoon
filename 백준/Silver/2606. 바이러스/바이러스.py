#dfs 로 구현하기
#재귀함수 구현
#주어진 노드를 그래프화 -> for 문을 돌려서 찾기
# 첫째줄 컴퓨터 수 둘째줄 쌍
com = int(input())
pair =int(input())
graph=[[0]*(com+1) for _ in range(com+1)]
visited=[False] * (com+1)
for i in range(pair):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1
cnt=0


def dfs(n,graph,visited):
    global  cnt

    visited[n]= True
    for k in range(1,com+1):
        if graph[n][k]==1 and visited[k]==False:
            cnt+=1
            dfs(k,graph,visited)

dfs(1,graph,visited)
print(cnt)

