def solution(n, k):
    answer = []
    people = [i for i in range(1,n+1)] # 해당 사람이 줄을서면 0으로 변환
    
    
    
    while n>0:
        pact_n = getpact(n)//n 
        
        if k % pact_n :
            getpeople = k // pact_n 
        else:
            getpeople = k // pact_n - 1
        answer.append(people.pop(getpeople))
        k=k%pact_n
        n-=1
        
    return answer
                      
                      
def getpact(n):
        num =1
        while n>1:
            num *= n
            n-=1
        return num
    
                         