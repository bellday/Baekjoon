def solution(a, b):
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    days=0
    for num in range(a-1):
        days+=month[num]
    days= days +b
    print(days)
    if (days-1)%7 ==0:
        return "FRI"
    elif (days-1)%7 ==1:
        return "SAT"
    elif (days-1)%7 ==2:
        return "SUN"
    elif (days-1)%7 ==3:
        return "MON"
    elif (days-1)%7 ==4:
        return "TUE"
    elif (days-1)%7 ==5:
        return "WED"
    elif (days-1)%7 ==6:
        return "THU"