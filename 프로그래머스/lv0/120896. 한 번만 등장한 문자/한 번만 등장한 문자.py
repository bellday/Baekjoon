def solution(s):
    num = 0
    dict_str={}
    for str_s in s:
        if str_s in dict_str:
            dict_str[str_s]+=1
        else:
            dict_str[str_s]=1
            
    dict_str = {key: value for key, value in dict_str.items() if value == 1}     
    return ''.join(sorted(dict_str.keys()))


