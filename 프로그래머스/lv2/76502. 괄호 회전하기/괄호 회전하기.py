def solution(s):
    len_s=len(s)
    s=s*2
    last_word=''
    string_list=[]
    answer = 0
    for i in range(len_s):
        check=s[i:i+len_s]
        cnt=0
        for c in check:
            if len(string_list) >0:
                if c==')' and string_list[-1] == '(':
                    string_list.pop()
                elif c==']' and string_list[-1] == '[':
                    string_list.pop()
                elif c=='}' and string_list[-1] == '{':
                    string_list.pop()
                else:
                    string_list.append(c)
            
            else:
                string_list.append(c)
        if len(string_list)==0:
            answer+=1
        string_list=[]
            
            
                
                        
                
        
    return answer