def solution(board, skill):
    answer = 0
    board1 = [[0] * (len(board[0])+1)  for _ in range(len(board)+1)]
    effect = []
    for s in skill:
        # 공격
        if s[0] == 1:
            board1[s[1]][s[2]] -= int(s[5])
            board1[s[3] + 1][s[2]] += int(s[5])
            board1[s[1]][s[4] + 1] += int(s[5])
            board1[s[3] + 1][s[4] + 1] -= int(s[5])


        # 회복
        elif s[0] == 2:

            board1[s[1]][s[2]] += int(s[5])
            board1[s[3] + 1][s[2]] -= int(s[5])
            board1[s[1]][s[4] + 1] -= int(s[5])
            board1[s[3] + 1][s[4] + 1] += int(s[5])
    for i in range(len(board)):

        for j in range(len(board[0])):
            board1[i][j + 1] += board1[i][j]

    for j in range(len(board[0])):

        for i in range(len(board)):
            board1[i + 1][j] += board1[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j]+= board1[i][j]
            if board[i][j]>=1:
                answer+=1
    return answer