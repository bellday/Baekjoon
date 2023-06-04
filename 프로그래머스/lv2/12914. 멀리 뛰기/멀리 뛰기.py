def solution(n):
    dict = {}
    
    dict[0] = 1
    dict[1] = 1
        
    for i in range(2, n+1):
        dict[i] = dict[i-1] + dict[i-2]
    
    answer = dict[n] % 1234567 
    return answer