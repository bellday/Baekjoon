def solution(number, k):
    answer = ''
    cnt=0
    num_list=[]
    for i in number:
        
        if len(num_list) ==0:
            num_list.append(i)
        else:
            while True:
                
                if len(num_list)==0 :
                    num_list.append(i)
                    break
                elif num_list[len(num_list)-1]>=i:
                    num_list.append(i)
                    break
                else:
                    if cnt < k:
                        num_list.pop()
                        cnt+=1
                    else:
                        num_list.append(i)
                        break
    if cnt != k:
        while True:
            
            if cnt == k:
                break
            
            num_list.pop()
            cnt+=1
    
                
            
    return ''.join(num_list)