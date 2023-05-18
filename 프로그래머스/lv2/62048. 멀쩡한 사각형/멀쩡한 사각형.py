#최대공배수에서 몇개를 빼야하는지 계산한 후
#전체에서 빼야하는 수 * case들 곱하기 
def solution(w,h):
    answer = 1
    all_square = w*h
    devide_max =0
    for i in range(1,min(w,h)+1):
        if w%i ==0 and h % i ==0:
            devide_max = i
    w= w//devide_max
    h= h//devide_max
    consume =  w+h-1
    answer = all_square - (devide_max * consume)
    return answer