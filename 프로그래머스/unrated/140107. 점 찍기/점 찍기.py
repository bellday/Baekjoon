#answer : 점의 수 카운트
# y축의 값 계산 ->  x축 값 증가 y값이 가능할때까지 -k 하기
# dlgn 0부터 k 까지 값 더하기
def solution(k, d):
    x=0;y=0
    answer = 0
    range_max = d//k #x 와 y가 최대로 이동할 수 있는 수
    height= 1+ range_max #x 가 0일 경우 계산
    answer = height
    max_y = k*(height-1)
    for i in range(1,range_max+1):
        x=i*k
        while True:
            
            if d*d >= x*x +max_y*max_y:
                mount = max_y//k+1
                
                answer+=mount
                break
                
            else:
                max_y= max_y -k
    
    
    return answer