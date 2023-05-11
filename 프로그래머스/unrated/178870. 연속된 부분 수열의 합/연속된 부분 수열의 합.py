#투포인터 알고리즘 사용
#k 값보다 작으면 두번째 포인터 값 추가
#k 값이 크면 첫번째 포인터 이동

def solution(sequence, k):
    answer = []
    left=0
    right=0
    sum_ = sequence[0]
    while left <= right and right < len(sequence):
        if sum_ == k:
            answer.append([left, right])
            sum_ -= sequence[left]
            left += 1
        elif sum_ < k:
            right += 1
            if right < len(sequence):
                sum_ += sequence[right]
        else:
            sum_ -= sequence[left]
            left += 1
    
    answer.sort(key = lambda x : (x[1]-x[0], x[0]))
    
    return answer[0]