def solution(array):
    count =0
    answer=''
    for i in array:
        answer+=str(i)
    for num in answer:
        if num =="7":
            count+=1
    return count