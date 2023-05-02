#ㅅt만큼 진행
def solution(n, t, m, p):
    answer = ''
    num=''
    num_to_string=[]
    change={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    change_v={v:k for k,v in change.items()}
    j=0
    len_t=t
    #진수변환
    t=t*m
    for i in range(t+1):
        if len(num) !=0:
            answer+=num[::-1]
            num=''
        while True:
            
            if i//n ==0:
                if i%n < 10:
                    num+=str(i%n)
                else:
                    num+=change_v.get(i%n)
                break
            else:
                if i%n < 10:
                    num+=str(i%n)
                else:
                    num+=change_v.get(i%n)
                i=i//n
    num=''
    #print(answer)
    
        
    for a in range(len(answer)):
        if a%m==p-1:

            num+=answer[a]
    num=num[:len_t]
        
    return num