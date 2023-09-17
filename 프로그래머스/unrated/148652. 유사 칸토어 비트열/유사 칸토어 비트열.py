def f(n,k):
    if n==1:
        return k if k<=2 else k-1
    
    div = 5**(n-1) # 나눌 수 (현재 n보다 하나 작은거로 나눠서, 항상 5개의 구역으로 나눌 수 있도록 함)
    mul = 4**(n-1) # 1의 개수
    loc = k//div # 5개로 나눴을 때 위치 0 1 2 3 4
    
    if k%div==0: # 딱 5로 나누어떨어졌을 때
        loc-=1
    
    if loc <2: # 11<- 011
        return mul*loc + f(n-1,k- loc*div)
    elif loc == 2: # 0 part
        return mul*loc
    else: # 110 11<-
        return mul*(loc-1) + f(n-1,k- loc*div) 

def solution(n, l, r):
    return f(n,r) - f(n,l-1)