'''
경우의 수 고려하기
기지국으로부터 -w +w 만큼 커버가능
만약 다음 기지국이 이전 기지국과 겹치면 면적 갱신하기
갱신한 후 아직 비어있는 곳 커버하기
비어있는곳 / (2*w)+1 을 통해서 확인
최종적으로 n까지 못돌았을 경우 마지막 부분을 전파못한것으로 간주하고 한번 더 돌린다.


'''


def solution(n, stations, w):
    answer = 0
    station = []
    #커버 가능한 범위 구하기
    for s in stations:
        
        start = s -w
        if start < 1:
            start = 1
        end = s+ w
        if end > n:
            end = n
        
        if len(station) > 0 and station[len(station)-1][1]+1 >=start:
            prev_start , prev_end = station.pop()
            station.append([prev_start,end])
        else:
            station.append([start,end])
    apt_start =1 ;apt_end = n
    #기지국 사이 몇대 설치할지 정하기
    for i in station:
        notConnect = (i[0] - apt_start)
        if (notConnect/ (2*w+1)) == (notConnect// (2*w+1)):
            answer +=notConnect// (2*w+1)
        else:
            answer += (notConnect// (2*w+1))+1
        apt_start = i[1]+1
    #아파트 n까지 안돌았을 경우 체크하기
    if apt_start <= n:
        leftConnect = n- apt_start+1
        if (leftConnect/ (2*w+1)) == (leftConnect// (2*w+1)):
            answer +=leftConnect// (2*w+1)
        else:
            answer += (leftConnect// (2*w+1))+1
    
    

    return answer