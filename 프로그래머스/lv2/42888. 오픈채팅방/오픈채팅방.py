#Enter : NickName , 들어왔습니다.
#Change : NickName
#Leave  :NickName , 나갔습니다.

def solution(record):
    answer = []
    rst=[]
    user_dict={}
    for r in record:
        
        log= r.split(' ')
        InOut = log [0]
        UserId = log [1]
        if InOut == 'Enter':
            NickName = log[2]
            user_dict[UserId] = NickName
            answer.append(UserId +"1")
            
        elif InOut == 'Change':
            NickName = log[2]
            user_dict[UserId] = NickName
        elif InOut == 'Leave':
            answer.append(UserId +"2")
    for a in answer:
        
        if a[-1:] == "1":
            rst.append(user_dict[a[:-1]] + "님이 들어왔습니다.")
        elif a[-1:] == "2":
            rst.append(user_dict[a[:-1]]+ "님이 나갔습니다.")
        
    return rst