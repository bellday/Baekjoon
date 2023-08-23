def solution(myString):
    answer = ''
    for i in myString:
        if i.isupper() == True:
            answer +=i
        else:
            i=i.upper()
            answer +=i
    return answer