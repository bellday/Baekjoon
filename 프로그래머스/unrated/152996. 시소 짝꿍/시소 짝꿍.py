
def solution(weights):
    answer = 0
    temp=0
    dic_weights = {}
    for w in weights:
        if w not in dic_weights:
            dic_weights[w]=1
        else:
            dic_weights[w]+=1
    for i in dic_weights:
        
        if dic_weights[i]>=2:
            answer += int(dic_weights[i]*(dic_weights[i]-1) /2)
        if i*2/3 in dic_weights:
            temp +=dic_weights[i]*dic_weights[i*2/3]
            
        if i*2 in dic_weights:
            temp +=dic_weights[i]*dic_weights[i*2]
            
        if i*3/2 in dic_weights:
            temp +=dic_weights[i]*dic_weights[i*3/2]
            
        if i*3/4 in dic_weights:
            temp +=dic_weights[i]*dic_weights[i*3/4]
            
        if i*1/2 in dic_weights:
            temp +=dic_weights[i]*dic_weights[i*1/2]
            
        if i*4/3 in dic_weights:
            temp +=dic_weights[i]*dic_weights[i*4/3]
            
    
    return answer+temp/2