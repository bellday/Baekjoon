#좌표 밖 무시하기
def solution(dirs):
    answer = 0
    graph=[[0]*11 for _ in range(11)]
    visited=set()
    sx=5
    sy=5
    graph[sx][sy]=1
    
    cnt=0#방문여부 체크
    
    for d in dirs:#방향
        
        if  d=="U":#올라갈 경우
            nx= sx-1
            ny= sy
            if 0<=nx<11 and  0<= ny<11: #좌표안일경우
                visited.add((sx,sy,nx,ny))
                visited.add((nx,ny,sx,sy))
                    
                    
                #이동한 값을x,y로 설정
                sx=nx
                sy=ny
                
        if  d=="D":#올라갈 경우
            nx= sx+1
            ny= sy
            if 0<=nx<11 and  0<= ny<11: #좌표안일경우
                visited.add((sx,sy,nx,ny))
                visited.add((nx,ny,sx,sy))
                    
                    
                #이동한 값을x,y로 설정
                sx=nx
                sy=ny
                
        if  d=="R":#올라갈 경우
            nx= sx
            ny= sy+1
            if 0<=nx<11 and  0<= ny<11: #좌표안일경우
                visited.add((sx,sy,nx,ny))
                visited.add((nx,ny,sx,sy))
                    
                    
                #이동한 값을x,y로 설정
                sx=nx
                sy=ny
        if  d=="L":#올라갈 경우
            nx= sx
            ny= sy-1
            if 0<=nx<11 and  0<= ny<11: #좌표안일경우
                visited.add((sx,sy,nx,ny))
                visited.add((nx,ny,sx,sy))
                    
                    
                #이동한 값을x,y로 설정
                sx=nx
                sy=ny
    
    return len(visited)//2