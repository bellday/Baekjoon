def solution(n):
    answer = [0]
    columns = [False] * n
    diagonals1 = [False] * (2 * n - 1)  # 왼쪽 위에서 오른쪽 아래로 향하는 대각선 (/) 방향 검사
    diagonals2 = [False] * (2 * n - 1)  # 왼쪽 아래에서 오른쪽 위로 향하는 대각선 (\) 방향 검사

    def backtracking(row):
        if row == n:
            answer[0] += 1
            return

        for col in range(n):
            if not columns[col] and not diagonals1[row + col] and not diagonals2[row - col + n - 1]: #3개 다 아닐경우
                columns[col] = diagonals1[row + col] = diagonals2[row - col + n - 1] = True # true 로해서 탐색 진행
                backtracking(row + 1)
                columns[col] = diagonals1[row + col] = diagonals2[row - col + n - 1] = False #복구

    backtracking(0)
    return answer[0]
