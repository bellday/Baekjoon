# key ,lambda 로 정렬 구현
# row_begin 부터 row_end 까지 for 문을 돌며 순회
# mod 값으로 최신화
# 합한값을 ^= 통해 xor  계산
def solution(data, col, row_begin, row_end):
    answer = 0
    s=0
    data = sorted(data , key = lambda x : (x[col-1],-x[0]))
    
    
    for i in range(row_begin-1,row_end):
        s=0
        for j in range(len(data[i])):
            temp = data[i][j]
            data[i][j] = temp%(i+1)
        
        s+=sum(data[i])  
        answer ^= s
        
        #print(answer)
    
    
    return answer