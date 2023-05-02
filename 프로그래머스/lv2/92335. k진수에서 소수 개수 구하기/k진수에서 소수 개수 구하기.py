def solution(n, k):
    answer = 0
    trans_num=''
    num_list=[]
    check=''
    cnt=0
    while True:
        
        if n//k==0:
            trans_num +=str(n%k)
            break
        trans_num +=str(n%k)
        n=n//k
    trans_num=trans_num[::-1]
    
    for t in range(len(trans_num)):
        
        
        if int(trans_num[t])==0:
            if len(check)!=0:
                num_list.append(int(check))
                check=''
        else:
            check+=trans_num[t]
    if len(check) !=0:
        num_list.append(int(check))
    
    for n in num_list:
        cnt=0
        if n==1:
            cnt+=1
        for i in range(2,int(n**(1/2))+1):
            
            if n% i ==0:
                cnt+=1
                break
        if cnt ==0:
            answer+=1
    
    return answer