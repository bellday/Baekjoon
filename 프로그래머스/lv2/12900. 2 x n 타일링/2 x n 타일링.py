# 1,2,3,5,8
def solution(n):
    answer = 0
    num_list=[1,2]
    for i in range(2,n):
        
        case=num_list[i-1]+num_list[i-2]
        num_list.append(case%1000000007)
    answer=num_list[len(num_list)-1]
    return answer