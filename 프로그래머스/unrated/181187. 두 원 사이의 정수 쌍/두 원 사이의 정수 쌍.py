def solution(r1, r2):
    answer = 0
    h1=r1
    h2=r2
    
    for i in range(1,r1):
        
        while h1*h1 + i*i >r1*r1:
            h1-=1
        if h1*h1 + i*i ==r1*r1:
            answer-=(h1-1)
        else:
            answer-=h1
            
    for j in range(1,r2):
        while h2*h2 + j*j >r2 * r2:
            h2-=1
        answer+=h2
    answer*=4
    answer +=4*(r2-r1+1)
    return answer