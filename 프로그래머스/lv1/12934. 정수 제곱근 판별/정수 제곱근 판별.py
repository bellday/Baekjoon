def solution(n):
    answer = 0
    num =n**(1/2)
    if  n % num ==0:
        return (num+1)**(2)
    else:
        return -1