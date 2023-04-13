def solution(A,B):
    answer = 0
    result1=0
    result2=0
    A.sort(reverse= True)
    B.sort()
    for i in range(len(A)):
        result1+=A[i]*B[i]
        result2+=A[i]*B[len(A)-i-1]
    if result1 >result2:
        return result2
    else:
        return result1