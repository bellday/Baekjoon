def solution(participant, completion):
    answer = ''
    dict_player={}
    for i in participant:
        
        if i not in dict_player:
            dict_player[i]=1
        else:
            dict_player[i]+=1
    for s in completion:
        if s in dict_player:
            dict_player[s]-=1
    for k, v in dict_player.items():
        if v == 1:
            return k
