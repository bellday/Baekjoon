
def find(x,visit):
    
    if visit[x] ==x:
        return x
    return find(visit[x],visit)
    
    
def union(a,b,visit):
    
    a= find(a,visit)
    b= find(b,visit)
    
    if a > b:
        visit[b] = a
    else:
        visit[a] = b
        
def solution(n, costs):
    answer = 0
    visit = [0] * (n+1)
    costs= sorted(costs, key = lambda x: x[2])
    for i in range(1,n+1):
        visit[i] = i
    for cost in costs:
        
        if find(cost[0],visit) != find(cost[1],visit):
            union(cost[0], cost[1], visit)
            answer += cost[2]
    return answer
        