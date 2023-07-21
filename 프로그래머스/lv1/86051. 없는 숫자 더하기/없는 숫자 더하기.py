def solution(numbers):
    list_num = [0,1,2,3,4,5,6,7,8,9]
    answer = 0
    for num in list_num:
        if num not in numbers:
            answer+=num
    return answer