def solution(board):
    BoardWidth = len(board[0])
    BoardLength = len(board)
    answer = 0
    for i in range(1,BoardLength):
        for j in range(1,BoardWidth):
            if board[i][j] ==1:
                board[i][j] = min(board[i-1][j],board[i-1][j-1],board[i][j-1])+1
    for i in range(BoardLength):
        for j in range(BoardWidth):
            if answer < board[i][j]:
                answer = board[i][j]
    return answer*answer