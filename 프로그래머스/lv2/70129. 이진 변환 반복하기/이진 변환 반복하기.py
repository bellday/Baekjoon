def solution(s):
    cnt=0
    rt=0 #0의갯수
    while s!='1':
        rt+=len(s)-s.count('1')
        s=bin(s.count('1'))[2:]
        cnt+=1    
    answer = []
    answer.append(cnt)
    answer.append(rt)
    return answer