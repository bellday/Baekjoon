#단어 들어있으면 한글자 더하기


def solution(msg):
    word=''
    #0번째 단어 입력
    answer =['0']
    result=[]
    for _ in range(65,91):
        answer.append(chr(_))
    len_msg=len(msg)
    i=0
    
    while True:
        
        #종료조건
        if i == len_msg:
            
            if word in answer:
                result.append(answer.index(word))
            break
        word+=msg[i]
        i+=1
        
        if word not in answer:
            answer.append(word)
            result.append(answer.index(word[:-1]))
            word=''
            i=i-1
    
    return result