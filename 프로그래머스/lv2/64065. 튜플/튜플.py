def solution(s):
    answer = []
    s=s[2:-2]
    s =s.split("},{")
    
    #길이별로 분류
    s.sort(key = len)
    
    for i in s:
        ii = i.split(',')
        
        for k in ii:
            if int(k) not in answer:
                answer.append(int(k))
    return answer