def solution(order):
    stack=[]
    odr=0
    i=1
    while i != len(order)+1:
        stack.append(i)
        while stack and stack[-1]==order[odr]:
            odr+=1
            stack.pop()
        i+=1
    

    
        
    return odr