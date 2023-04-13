def solution(s):
    s=list(map(int,s.split()))
    print(s)
    print(max(s))
    print(min(s))
    answer = ''
    answer+=str(min(s))
    answer+=' '
    answer+=str(max(s))
    return answer