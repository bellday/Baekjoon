def dfs(node, graph, visit):
    visit[node] = True
    for i in range(len(graph)):
        if graph[node][i] == 1 and not visit[i]:
            dfs(i, graph, visit)
            

def solution(n, computers):
    a=1
    graph = [[0] * n for _ in range(n)]
    visit = [False] * n
    cnt = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i][j] = 1

    for i in range(n):
        if not visit[i]:
            dfs(i, graph, visit)
            cnt += 1
    

    return cnt