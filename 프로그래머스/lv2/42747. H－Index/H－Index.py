def solution(citations):
    answer = 0
    citations.sort()
    for i in range(1,max(citations)+1):
        big=0
        small=0
        for c in citations:
            #h번 이상 인용된 논문
            if i <= c:
                big+=1
            #나머지 논문
            else :
                small +=1
        if big >=i and small <=i:
            answer=i
    return answer