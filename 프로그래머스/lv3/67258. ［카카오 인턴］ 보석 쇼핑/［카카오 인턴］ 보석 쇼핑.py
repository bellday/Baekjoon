'''
알고리즘 : 투포인터
모든 종류의 보석을 포함하는 구간을 찾으면 
L 를 니동시키며 가장 짧은 구간을 찾는다.
만약 못찾으면 R값을 증가시킨다.

'''
def solution(gems):
    answer = [-1,len(gems)] # 초기 길이 설정
    CaseGems = len(set(gems))
    DictGems = {gems[0]:1}
    left = 0; right = 0
    
    while left < len(gems) and right < len(gems):
        
        if len(DictGems) == CaseGems:
            
            if (right - left) < (answer[1] -answer[0]):
                answer[1] = right+1
                answer[0] = left+1
            else:
                DictGems[gems[left]] -=1
                if DictGems[gems[left]] ==0:
                    del DictGems[gems[left]]
                left +=1
        
        else:
            right += 1

            if right == len(gems):  # index 넘어가지 않도록 구현
                break
        
            if gems[right] in DictGems:  # 딕셔너리 key에 있으면 count
                DictGems[gems[right]] += 1

            else:  # 없으면 추가
                DictGems[gems[right]] = 1
            
            

    
    
    return answer