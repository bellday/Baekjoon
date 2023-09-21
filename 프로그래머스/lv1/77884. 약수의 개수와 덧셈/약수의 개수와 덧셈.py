def solution(left, right):
    answer = 0
    for num in range(left,right+1,1):
        n= num**(1/2)
        if num%n==0:
            answer=answer- num    
        else:
            answer=answer+num
    return answer