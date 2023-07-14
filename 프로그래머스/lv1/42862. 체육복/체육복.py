def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    reserve_1 = set(reserve)-set(lost)
    lost_1 = set(lost)-set(reserve)
    for i in reserve_1:
        if i in lost: #여벌 체육복을 가져온 학생들
            lost_1.remove(i)
            
        elif i-1 in lost_1:#앞번호 학생 체육복 빌려주기
            lost_1.remove(i-1)
        elif i+1 in lost_1:#뒷번호 학생 체육복 빌려주기
            lost_1.remove(i+1)
    
    return n- len(lost_1)