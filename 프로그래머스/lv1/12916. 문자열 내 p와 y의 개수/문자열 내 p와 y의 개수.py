def solution(s):
    a = s.count("P")+s.count("p")
    b = s.count("Y")+s.count("y")
    if a==b:
        return True
    else:
        return False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.