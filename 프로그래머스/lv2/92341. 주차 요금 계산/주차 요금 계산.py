#fees[0]: 기본시간 fees[1]: 기본요금 fees[2]: 단위시간 fees[3]: 단위 요금
# 계산 방법 : (총시간 - 기본시간(fees[0])) // 단위시간 * 단위 요금 + 기본요금
#딕셔너리 2개를 통해서 종합하기

def solution(fees, records):
    answer = []
    dict_cars={}#차량 입출입
    TimeRegister={}# 차량 입출입하고서 계산한 시간
    
    LastTime= 23*60 + 59
    for r in records:
        time= int(r[:2]) *60 + int(r[3:5])
        
        car_num=r[6:10]
        in_out=r[11:]
        
        # 차가 들어올 경우
        if in_out == "IN":
            dict_cars[car_num] = time
            if car_num not in TimeRegister:
                TimeRegister[car_num] = 0
            
        #차가 빠져나올 경우
        else:
            StayTime = time - dict_cars[car_num]
            TimeRegister[car_num] += StayTime
            del dict_cars[car_num]
        
        #차가 있는지 여부 파악하기
    if len(dict_cars) >0:
            
        for car in dict_cars:
            LeftCar = LastTime - dict_cars[car]
            TimeRegister[car]+= LeftCar
    TR = sorted(TimeRegister) # TR은 정렬된 딕셔너리
    
    for t in TR:
        AllTime = TimeRegister[t]
        
        # 기본요금만 계산할지 여부 파악
        # 기본시간보다 작을경우 기본요금만 추가
        if AllTime < fees[0]:
            answer.append(fees[1])
            
        else:
            RemainTime = AllTime - fees[0]
            
            #시간이 남을 경우 올림
            
            if RemainTime% fees[2] != 0: 
                RemainTime = RemainTime // fees[2] +1
            else:
                RemainTime = RemainTime // fees[2]
            answer.append(fees[1] + RemainTime* fees[3])
    return answer