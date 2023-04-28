#소모필요도 보다 크다면 카운팅 , k- 소모피로도를 k에 대입
#8! 가지수 구하기
from itertools import permutations

def solution(k, dungeons):
    dun_num = len(dungeons)
    answer = 0
    
    for permut in permutations(dungeons, dun_num):
        hp=k
        count=0
        for p in permut:
            if hp>=p[0]:
                hp=hp-p[1]
                count+=1
        
        if answer<count:
            answer=count
    return answer