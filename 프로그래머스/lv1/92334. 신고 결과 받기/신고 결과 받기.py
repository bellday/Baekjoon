def solution(id_list, report, k):
    answer = []
    remove_list=[]
    dict_id={}
    stop_dic={}
    for i in id_list:#딕셔너리로 설정
        dict_id[i]=0
        stop_dic[i]=0
    for r in list(set(report)):#받은 사람들 카운트
        loc=r.index(' ')
        dict_id[r[loc+1:]]+=1
        
    for key,v in dict_id.items():#K값과 같거나 커서 정지예정자 리스트
        if v>=k:
            remove_list.append(key)
    for r in list(set(report)):#받은 사람들 카운트
        loc=r.index(' ')
        if r[loc+1:]  in remove_list:
            stop_dic[r[:loc]]+=1
    for keyy,value in stop_dic.items():
        answer.append(value)
        
    return answer