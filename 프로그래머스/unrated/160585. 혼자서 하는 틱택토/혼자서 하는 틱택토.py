# ox 차이
# o 가1ㄱ 더이을 경우


def solution(board):
    answer = 1
    o_cnt = 0
    x_cnt = 0
    finish_ocnt =0
    finish_xcnt =0 
    len_board = len(board)
    for k in range(len_board):
        
        if board[k][0]=='O'and board[k][1]=='O' and board[k][2]=='O':
            finish_ocnt +=1
        if board[0][k]=='O' and board[1][k]=='O' and board[2][k]=='O':
            finish_ocnt +=1
        if board[k][0]=='X'and board[k][1]=='X' and board[k][2]=='X':
            finish_xcnt +=1
        if board[0][k]=='X' and board[1][k]=='X' and board[2][k]=='X':
            finish_xcnt +=1
    
    if board[0][0]=='O'and board[1][1]=='O' and board[2][2]=='O':
            finish_ocnt +=1
    if board[2][0]=='O'and board[1][1]=='O' and board[0][2]=='O':
            finish_ocnt +=1
    if board[0][0]=='X'and board[1][1]=='X' and board[2][2]=='X':
            finish_xcnt +=1
    if board[2][0]=='X' and board[1][1]=='X' and board[0][2]=='X':
            finish_xcnt +=1
    
    for i in range(len_board):
        for j in range(len_board):
            if board[i][j] == 'O':
                o_cnt +=1
            elif board[i][j] == 'X':
                x_cnt +=1
    if (finish_xcnt >= 1 and finish_ocnt >=1) or (o_cnt>x_cnt+1) or (x_cnt>o_cnt):
        return 0
    if finish_xcnt ==1 and o_cnt!=x_cnt:
        return 0
    elif finish_ocnt ==1 and x_cnt+1 !=o_cnt:
        return 0
    return answer