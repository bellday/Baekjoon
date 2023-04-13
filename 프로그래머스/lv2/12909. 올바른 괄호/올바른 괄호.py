def solution(s):
    list_s=[]
    for i in s:
        if i==")" and len(list_s)==0:
            return False
        elif i==")":
            list_s.pop()
        else:
            list_s.append(i)
    print(len(list_s))
    if len(list_s)==0:
        return True
    else:
        return False