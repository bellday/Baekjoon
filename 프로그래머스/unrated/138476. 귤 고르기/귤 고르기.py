#가장많은 갯수를 뺀다.
# k 와 갯수를 비교하여 갯수가 같거나 많은경우
# k의 갯수가 더 클경우 cnt +1 하고 다음으로 많은 수를 찾아서 연산
def solution(k, tangerine):
    answer = 0
    dict_t={}
    for t in tangerine:
        if t not in dict_t:
            dict_t[t]=1
        else:
            dict_t[t]+=1
    
    sort_dict_i=sorted(dict_t.items(), key=lambda x: x[1], reverse=True)
    
    for key,v in sort_dict_i:
        
        if v>=k:
            answer+=1
            return answer
        else:
            k=k-v
            answer+=1
            
    