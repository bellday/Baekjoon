def solution(n, m):
    answer = []
    list_num =[]
    for num in range(2,max(n,m)+1):
        if n% num ==0 and m% num==0:
            list_num.append(num)
    if len(list_num)==0:
        answer.append(1)
    else:
        answer.append(list_num[len(list_num)-1])
    for number in range(max(n,m),1000001):
        if number% n ==0 and number %m ==0:
            answer.append(number)
            break
    return answer
    