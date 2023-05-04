def solution(n):
    answer = 0
    num_list=[3,11]
    if n%2 ==1:
        return answer
    
    elif n==2:
        return 3

    elif n==4:
        return 11
    else:
        for i in range(6,n+1,2):
            num = i//2
            num_list.append((num_list[num-2]*4 - num_list[num-3])%1000000007)
    return num_list[len(num_list)-1]
            
            