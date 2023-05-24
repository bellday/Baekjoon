def solution(topping):
    answer = 0
    dic_chulsu = {}
    dic_brother = {}
    for t in range(len(topping)):
        if topping[t] not in dic_chulsu:
            dic_chulsu[topping[t]] =1
        else:
            dic_chulsu[topping[t]] +=1
    chulsu = len(dic_chulsu)
    brother = len(dic_brother)
    for t in range(len(topping)):
        
        if topping[t] not in dic_brother:
            dic_brother[topping[t]] =1
            dic_chulsu[topping[t]] -=1
            brother+=1
        else:
            dic_brother[topping[t]] +=1
            dic_chulsu[topping[t]] -=1
        if dic_chulsu[topping[t]] ==0:
            chulsu -=1
        if brother == chulsu:
            answer+=1
    
        
    return answer