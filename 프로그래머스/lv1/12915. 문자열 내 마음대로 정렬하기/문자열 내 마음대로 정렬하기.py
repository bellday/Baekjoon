#string의 n번째를 앞에다가 추가함으로 정렬
#시간복잡도 : o(n^2),  배열sort
def solution(strings, n):
    answer = []
    dict_string=[]
    for i in strings:
        dict_string.append(i[n]+i)# string의 n번째를 앞에다가 추가
    dict_string.sort()
    for i in dict_string:
        answer.append(i[1:])
        
    return answer