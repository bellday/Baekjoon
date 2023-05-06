def solution(n,a,b):
    answer = 0
    
    while True:
        if a%2==1: #홀수일 경우
            a= a//2 +1
            #print('1',a)
        else:
            a= a//2
            #print('2',a)
        if b%2 ==1:
            b= b//2 +1
            #print('3',b)
        else:
            b= b//2
            #print('4',b)
        if a==b:
            answer+=1
            break
        else:
            answer+=1
            
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')

    return answer