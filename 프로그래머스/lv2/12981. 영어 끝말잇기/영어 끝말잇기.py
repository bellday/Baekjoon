#n보다 크면 1로
#딕셔너리로 체크
#
def solution(n, words):
    dict_word={}
    for index ,word in enumerate(words):
        if index>=1:
            if words[index][:1]!=words[index-1][-1:]:
                if (index+1)%n==0:
                    return [n,(index+1)//n]
                return [(index+1)%n,(index+1)//n+1]
        if word not in dict_word:
            dict_word[word]=0
        elif word in dict_word:
            if (index+1)%n ==0:
                return [n,(index+1)//n]
            else:
                return [(index+1)%n,(index+1)//n+1]
            
        
        

    return [0,0]