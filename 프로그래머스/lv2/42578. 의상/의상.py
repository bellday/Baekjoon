def solution(clothes):
    answer = 1
    dict_cloth={}
    for c in clothes:
        if c[1] in dict_cloth:
            dict_cloth[c[1]]+=1
        else:
            dict_cloth[c[1]]=1
    
    for d,item in dict_cloth.items():
        answer*=(item+1)
    return answer-1