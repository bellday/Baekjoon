def solution(dot):
    if dot[0]>0 and dot[1]>0: #1사분면
        return 1
    elif dot[0]<0 and dot[1]>0: #2사분면
        return 2
    elif dot[0]<0 and dot[1]<0: #3사분면
        return 3
    elif dot[0]>0 and dot[1]<0:# 4사분면
        return 4
    