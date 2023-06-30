'''
    4개의 블록 부수는 방향, 움직이는 방향 2가지로 구현
    부수는 방향에선 set함수로 중복 없애기
    움직이는 방향에선 아래로 0이 아닐때까지 계속 움직인다. 

'''
def solution(m, n, board):
    answer = 0
    graph = [[] for _ in range(m)]
    for g in range(m):
        for k in range(n):
            graph[g].append((board[g][k]))    
    while True:
        
        cnt = boom(graph)
        move(graph)
        
        if cnt ==0:
            break
        else:
            answer+=cnt       
    return answer

def boom(board):
    
    height = len(board)
    width = len(board[0])
    char_list = []
    for i in range(height):
        for j in range(width):
            
            if (i+1) < height and (j+1) < width:
                char1 = board[i][j]
                char2 = board[i+1][j]
                char3 = board[i+1][j+1]
                char4 = board[i][j+1]
                if char1 == char2 and char1 == char3 and char1 == char4 and char1 !="0":
                    char_list.append((i,j))
                    char_list.append((i+1,j))
                    char_list.append((i,j+1))
                    char_list.append((i+1,j+1))
    if len(char_list) > 0:
        char_list =set(char_list)
        #이동할 부분 표현
        for x in char_list:

            board[x[0]][x[1]] ="0"
    
    return len(char_list)

def move(board):
    height = len(board)
    width = len(board[0])
    
    while True:
        movement = 0 
        for i in range(height-1):
            
            for j in range(width):

                if board[i][j] != "0" and board[i+1][j] == "0":
                    temp = board[i][j]
                    board[i][j] = "0"
                    board[i+1][j] = temp
                    movement+=1
        if movement ==0:
            break
        
    
                
    
                
                