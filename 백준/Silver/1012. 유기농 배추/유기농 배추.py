from collections import deque

testcase = int(input())
db = [1, 0, -1, 0]  # 가로
da = [0, 1, 0, -1]  # 세로

for t in range(testcase):
    cnt = 0
    m, n, k = map(int, input().split())  # 가로 m , 세로 n, 배추개수 k
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for b in range(k):  # 배추의 개수 입력
        x, y = map(int, input().split())  # x가 가로 y 가 세로
        graph[y][x] = 1

    for i in range(n):  # i 세로
        for j in range(m):  # j 가로
            if graph[i][j] == 1 and not visited[i][j]:
                cnt += 1
                queue = deque([(i,j)])
                while queue:
                    a, b = queue.popleft()
                    visited[a][b] = True
                    for z in range(4):
                        na = a + da[z]
                        nb = b + db[z]
                        if 0 <= na < n and 0 <= nb < m and graph[na][nb] == 1 and not visited[na][nb]:
                            visited[na][nb] = True
                            queue.append((na,nb))

    print(cnt)