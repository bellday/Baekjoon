#124 3가지 숫자로 표현
# 3, 9 ,27 ...
# 3으로 나누었을 때 나머지 1인 경우 1
# 3으로 나누었을 때 나머지 2인 경우 2
#3으로 나누었을 때 나머지 1인 경우 1
def solution(n):
    answer = ''
    add_num=3
    while True:
        
        #다음 자리에 숫자가 있을 경우
        if n>add_num:
            
            if 0<n%add_num<=(add_num//3):
                answer='1'+answer
            elif add_num//3< n%add_num<=(2*add_num//3):
                answer='2'+answer
            elif n%add_num<=(3*add_num//3) or n%add_num ==0:
                answer='4'+answer
                
            n=n-add_num
            add_num=add_num*3
            
        #다음 자리에 숫자가 없으면
        else:
            if n<=(add_num//3):
                answer='1'+answer
            elif n<=(2*add_num//3):
                answer='2'+answer
            elif n<=(3*add_num//3):
                answer='4'+answer
            break
    return answer