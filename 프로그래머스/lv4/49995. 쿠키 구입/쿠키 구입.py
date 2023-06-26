def solution(cookie):
    answer = 0
    n = len(cookie)

    for i in range(n - 1):
        LeftSum, LeftIndex = cookie[i], i
        RightSum, RightIndex = cookie[i + 1], i + 1

        while True:
            if LeftSum == RightSum:
                answer = max(answer, LeftSum)
                
                
            if LeftIndex > 0 and LeftSum <= RightSum:
                LeftIndex -= 1
                LeftSum += cookie[LeftIndex]
            elif RightIndex < n - 1 and RightSum <= LeftSum:
                RightIndex += 1
                RightSum += cookie[RightIndex]
            else:
                break

    return answer