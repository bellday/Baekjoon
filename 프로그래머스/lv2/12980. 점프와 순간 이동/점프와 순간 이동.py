def solution(n):
    ans = 0
    bin_n=bin(n)
    
    ans=bin_n.count('1')
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')

    return ans