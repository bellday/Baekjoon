#처음 나왔을 경우 -1
# 이전에 나왔으면 현재 위치 - 이전 위치 값을  append
def solution(s):
    dict_s={}
    answer = []
    for index, string in enumerate(s):
        if string not in dict_s:#글자가 처음 나왔을 경우
            dict_s[string]=index
            answer.append(-1)
        else: #앞에 글자가 있을경우
            answer.append(index-dict_s[string])
            dict_s[string]= index
    print(dict_s)
    return answer