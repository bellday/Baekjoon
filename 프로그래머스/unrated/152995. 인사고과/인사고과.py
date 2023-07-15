def solution(scores):
    answer = 1
    wanho0 = scores[0][0]
    wanho1 = scores[0][1]
    wanho_score = wanho0+wanho1 
    th =0
    scores = sorted(scores, key=lambda x:(-x[0], x[1]))
    
    for score in scores:
        
        if score[0]> wanho0 and score[1] >wanho1:
            return -1
        if wanho_score < sum(score)  and th <= score[1]:
            answer+=1
            th =score[1]
                
    return answer