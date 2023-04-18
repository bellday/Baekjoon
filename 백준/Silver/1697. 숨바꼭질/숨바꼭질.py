from collections import deque
n,k = map(int,input().split())# n: 수빈 위치 , k : 동생이 있는 위치
visit=[0]* 100001
t=0


def bfs(n,t):
    queue=deque([(n,t)])
    while queue:

        num,t=queue.popleft()
        visit[num]=1
        if num == k:
            print(t)
            exit()
        if  0<=num-1<=100000:
            if visit[num-1]==0:
                queue.append((num-1,t+1))

        if 0<=num+1<=100000:
            if visit[num+1]==0:
                queue.append((num+1,t+1))

        if  0<=num*2<=100000:
            if visit[num*2]==0:
                queue.append((num*2,t+1))



bfs(n,t)
