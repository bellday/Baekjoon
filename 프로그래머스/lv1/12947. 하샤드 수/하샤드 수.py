def solution(x):
    list_x=list(str(x))
    sum_x=0
    for n in list_x:
        sum_x+=int(n)
    if x%sum_x ==0:
        return True
    else:
        return False
