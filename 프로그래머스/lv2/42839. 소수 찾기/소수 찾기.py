# 1부터 numbers 길이만큼 수행 
# 리스트에 없으면  추가하기
# 마지막에 for 문을 통해 해당 문자열을 숫자로 변환 후 소수여부 파악
from itertools import permutations
def solution(numbers):
    answer = 0
    num_list=[]
    for i in range(1,len(numbers)+1):
        
        for permut in permutations(numbers,i):
            num=''
            for p in permut:
                num+=p
            if int(num) not in num_list:
                num_list.append(int(num))
    for n in num_list:
        cnt=0
        if n>=2:
            for k in range(1,int(n**(1/2)+1)):
                if n%k ==0:
                    cnt+=1
        if cnt==1:
            answer+=1
            
    return answer