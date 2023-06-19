def solution(picks, minerals):
    answer = 0
    listMineral = []
    cnt = []
    check = 5;start =0
    #광물이 많다면 자르기
    if len(minerals) > sum(picks)*5:
        minerals = minerals[:sum(picks)*5]
    
    #광물을 3,2,1로 표현
    for m in minerals:
        if m == "diamond":
            listMineral.append(3)
            
        elif m == "iron":
            listMineral.append(2)
            
        elif m ==  "stone":
            listMineral.append(1)
            
    while True:
        
        if check > len(listMineral):
            check = len(listMineral)
        if start > len(listMineral) or start > sum(picks)*5:
            break
        pick_mineral = listMineral[start:check]
        Dia = pick_mineral.count(3)
        Iron = pick_mineral.count(2)
        Stone = pick_mineral.count(1)
        cnt.append((Dia,Iron,Stone))
        start +=5
        check +=5
    # 다이아 철 갯수 카운팅하기
    cnt = sorted(cnt, key = lambda x: (x[0], x[1]) , reverse = True)
    print(cnt)
    
    
    for i in cnt:
        
        if picks[0] > 0:
            temp = picks[0]
            picks[0] = temp -1
            PICK = 0
        elif picks[1] > 0:
            temp = picks[1]
            picks[1] = temp -1
            PICK = 1
        elif picks[2] > 0:
            temp = picks[2]
            picks[2] = temp -1
            PICK = 2
        
        
        if PICK == 0 : #다이아 몬드
            answer += i[0]
            answer += i[1]
            answer += i[2]
            
        elif PICK == 1: #철
            answer += i[0] *5
            answer += i[1]
            answer += i[2]
        elif PICK == 2: #돌
            answer += i[0] *25
            answer += i[1] * 5
            answer += i[2]
    print(picks)
    return answer