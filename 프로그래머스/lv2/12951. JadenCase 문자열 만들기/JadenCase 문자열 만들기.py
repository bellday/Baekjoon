#숫자는 첫 단어로만
# 숫자일 경우 나머지 단어는 소문자
# 만약 전 단계가 ' ' 이고 지금이 문자면 대문자
# 만약 전 단계가 ' ' 이고 지금이 숫자면 숫자, 나저미 소문자
def solution(s):
    answer = ''
    num_list=['1','2','3','4','5','6','7','8','9','0']
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if s[0]==' ':#빈칸이면 추가
        answer+=s[0]
    elif s[0] in num_list:#첫 글자가 숫자면 추가
        answer+=s[0]
    else:  #첫 글자가 단어면 대문자로 추가
        answer+=s[0].upper()
    print(answer)
    
    for i in range(1,len(s)):# 1부터 len(s) 까지
        if s[i].isalpha() and s[i-1]==' ':#첫 단어가 문자고 이전 단어가 ' '일 경우
            answer+=s[i].upper()
        elif s[i].isalpha():
            answer+=s[i].lower()
        else:
            answer+=s[i]
        
        
    return answer