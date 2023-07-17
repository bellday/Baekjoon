# 홀수일 경우  3글자면 [0,1,2] [1] 출력해야함 3/2 의 몫으로 구현
# 짝수일 경우  [1,2,3,4,5,6] [2,3] 출력해야함 4일경우 1,2 len(짝수)/2 len(짝수)-1 구하기
def solution(s):
    answer = ''
    s = list(s)
    print(s)
    if len(s)%2 == 0:
        answer +=s[(len(s)//2)-1]
        answer +=s[len(s)//2] 
         
    else:
        answer+=s[len(s)//2]
    return answer