def solution(s):
    num=["0","1","2","3","4","5","6","7","8","9"]
    if len(s)==4 or len(s) ==6:
        for string in s:
            if string not in num:
                return False
            
        answer = True
        return answer
    else:
        return False