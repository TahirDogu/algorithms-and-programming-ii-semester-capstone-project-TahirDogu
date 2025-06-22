def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(row, board, solutions):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1, board, solutions)

    solutions = []
    solve(0, [0]*n, solutions)
    return solutions


def step_by_step_solution(n):
    steps = []
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(row, board):
        if row == n:
            steps.append(board[:])
            return True
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                steps.append(board[:])
                if solve(row + 1, board):
                    return True
                steps.append(board[:])
        board[row] = -1
        return False

    solve(0, [-1]*n)
    return steps 
