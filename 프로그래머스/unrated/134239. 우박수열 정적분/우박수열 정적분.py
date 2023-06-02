def solution(k, ranges):
    answer = []
    point =[]
    cnt=0
    area=[]
    while True:
        point.append([cnt,k])
        if k==1:
            
            break
        if k%2 ==0:
            k = k//2
            cnt+=1
            
        else:
            k=3*k+1
            cnt+=1
            
    for i in range(cnt):
        area.append((point[i][1] + point[i+1][1])/2)
    
        
    for r in ranges:
        start=r[0]; end = cnt +r[1]
        if end < start:
            answer.append(-1)
        else:
            answer.append(sum(area[start:end]))
                
    return answer