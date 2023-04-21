def solution(want, number, discount):
    answer = 0
    dict_want={}
    for _ in range(len(want)):
        dict_want[want[_]]=number[_]
    
    for i in range(len(discount)-9):
        check_dict={}
        check=discount[i:i+10]
        for c in check:
            if c not in check_dict:
                check_dict[c]=1
            else:
                check_dict[c]+=1
        if check_dict==dict_want:
            answer+=1
    return answer