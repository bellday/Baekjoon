def dfs(n, Node, visit):
    # 방문 처리
    visit[n] = True
    cnt =1
    for i in Node[n]:
        
        if visit[i] == False:
            
            cnt +=dfs(i, Node, visit)

    return cnt


def solution(n, wires):
    answer = 100000000
    Node = [[] for _ in range(n + 1)]  # 계산 편하기 위해 더미 노드 추가
    
    # 와이어에 따른 노드 설정
    for w in wires:
        #print(w[0],w[1])
        Node[w[0]].append(w[1])
        Node[w[1]].append(w[0])

    visit = [False] * (n + 1)
    
    for t1, t2 in wires:
        # 노드 연결 끊기
        visit = [False] * (n + 1)
        visit2 = [False] * (n + 1)
        Node[t1].remove(t2)
        Node[t2].remove(t1)
        dfs1 = dfs(t1, Node, visit )
        dfs2 = dfs(t2, Node, visit2)


        answer = min(answer, abs(dfs1-dfs2))

        # 방문 후 다시  연결
        Node[t1].append(t2)
        Node[t2].append(t1)

    return answer