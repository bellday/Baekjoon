def solution(cards):
    card_list = [i for i in range(len(cards)+1)]
    visited = [0] * len(card_list)
    card_list = card_list[1:]
    dfs_list = []
    
    answer = 0
    for j in range(len(cards)):
        
        if visited[j] ==0: 
            visited[j]=1
            dfs(j,cards,visited,1,dfs_list)
    dfs_list.sort(reverse = True)
    
    if len(dfs_list)==1:
        return 0
    else:
        return dfs_list[0] * dfs_list[1]
    

def dfs(i,cards,visited, cnt,dfs_list):
    next_num = cards[i]-1
    if visited[next_num]==0:
        visited[next_num]=1
        dfs(next_num,cards,visited, cnt+1,dfs_list)
    else:
        dfs_list.append(cnt)
        return